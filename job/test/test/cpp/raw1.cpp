#include <stdio.h> 
#include <sys/types.h> 
#include <sys/socket.h> 
#include <netinet/in.h> 
#include <arpa/inet.h> 
#include <netdb.h> 
#include <unistd.h> 
#include <string.h> 
#include <stdlib.h> 
#include <netinet/ip_icmp.h> 
#include <time.h> 
#include <fcntl.h> 
#include <signal.h> 
#include <time.h> 
#define PACKETSIZE  64
struct packet {
    struct icmphdr hdr;
    char msg[PACKETSIZE-sizeof(struct icmphdr)];
};

int pid=-1;
int loops = 25;
struct protoent *proto=NULL;

unsigned short checksum(void *b, int len)  {   
	unsigned short *buf = b;
    	unsigned int sum=0;
    	unsigned short result;
    	for ( sum = 0; len > 1; len -= 2 )
        	sum += *buf++;
   	if ( len == 1 )
        	sum += *(unsigned char*)buf;
   	 sum = (sum >> 16) + (sum & 0xFFFF);
    	sum += (sum >> 16);
    	result = ~sum;
    	return result;
}
void display(void *buf, int bytes)  {  
     int i;
    struct iphdr *ip = buf;
        struct icmphdr *icmp = buf+ip->ihl*4;

        printf("----------------\n");
        for ( i = 0; i < bytes; i++ )        {
            if ( !(i & 15) ) printf("\n%04X:  ", i);
            printf("%02X ", ((unsigned char*)buf)[i]);
        }
        printf("\n");
        printf("IPv%d: hdr-size=%d pkt-size=%d protocol=%d TTL=%d src=%s ",
           ip->version, ip->ihl*4, ntohs(ip->tot_len), ip->protocol,
           ip->ttl, inet_ntoa(ip->saddr));
        printf("dst=%s\n", inet_ntoa(ip->daddr));
     if ( icmp->un.echo.id == pid )         {
            printf("ICMP: type[%d/%d] checksum[%d] id[%d] seq[%d]\n",
                   icmp->type, icmp->code, ntohs(icmp->checksum),
                   icmp->un.echo.id, icmp->un.echo.sequence);
        }
}
void listener(void)   {  
    int sd, i;
    struct sockaddr_in addr;
    unsigned char buf[1024];
    sd = socket(PF_INET, SOCK_RAW, proto->p_proto);
    if ( sd < 0 )       {
        perror("socket");
        exit(0);
    }
    for (i = 0; i < loops; i++)       {   
        int bytes, len=sizeof(addr);
        bzero(buf, sizeof(buf));
        bytes = recvfrom(sd, buf, sizeof(buf), 0, (struct sockaddr *) &addr, &len);
        if ( bytes > 0 )
            display(buf, bytes);
        else
            perror("recvfrom");
    }
    exit(0);
}
void ping(struct sockaddr_in *addr)
{   
    const int val=255;
        int i, j, sd, cnt=1;
        struct packet pckt;
     struct sockaddr_in r_addr;

     sd = socket(PF_INET, SOCK_RAW, proto->p_proto);
     if ( sd < 0 )
     {
        perror("socket");
         return;
        }
        if ( setsockopt(sd, SOL_IP, IP_TTL, &val, sizeof(val)) != 0)
            perror("Set TTL option");
        if ( fcntl(sd, F_SETFL, O_NONBLOCK) != 0 )
            perror("Request nonblocking I/O");
for (j = 0; j < loops; j++)       {  // send pings 1 per second
       int len=sizeof(r_addr);
        printf("Msg #%d\n", cnt);
        if ( recvfrom(sd, &pckt, sizeof(pckt), 0, (struct sockaddr *)&r_addr, &len) > 0 )
            printf("***Got message!***\n");
        bzero(&pckt, sizeof(pckt));
        pckt.hdr.type = ICMP_ECHO;
        pckt.hdr.un.echo.id = pid;
        for ( i = 0; i < sizeof(pckt.msg)-1; i++ )
            pckt.msg[i] = i+'0';
        pckt.msg[i] = 0;
        pckt.hdr.un.echo.sequence = cnt++;
        pckt.hdr.checksum = checksum(&pckt, sizeof(pckt));
        if (sendto(sd, &pckt, sizeof(pckt), 0, (struct sockaddr *) addr, sizeof(*addr)) <= 0)
            perror("sendto");
        sleep(1);
    }
}
int main(int count, char *argv[])   {   
   struct hostent *hname;
    struct sockaddr_in addr;
    loops = 0;
    if ( count != 3 )       {
        printf("usage: %s <addr> <loops> \n", argv[0]);
        exit(0);
    }
    if (count == 3)  // WE HAVE SPECIFIED A MESSAGE COUNT
        loops = atoi(argv[2]);
    if ( count > 1 )       {
        pid = getpid();
        proto = getprotobyname("ICMP");
        hname = gethostbyname(argv[1]);
        bzero(&addr, sizeof(addr));
        addr.sin_family = hname->h_addrtype;
        addr.sin_port = 0;
        addr.sin_addr.s_addr = *(long*)hname->h_addr;
        if ( fork() == 0 )
            listener();
        else
            ping(&addr);
        wait(0);
    }
    else
        printf("usage: myping <hostname>\n");
    return 0;
}