#include <sys/socket.h>
#include <resolv.h>
#include <netinet/in.h>
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
#define DEFDATALEN 64
#define MAXIPLEN 64
#define MAXICMPLEN 64
static void ping(const char *host)
{
 struct hostent *h; // structure stores, host name, address, any aliases for host
 struct sockaddr_in pingaddr; // create the socket address for ping target
 struct icmp *pkt; // ICMP Header
 int pingsock, c;
 char packet[DEFDATALEN + MAXIPLEN + MAXICMPLEN]; // max length

 if ((pingsock = socket (AF_INET, SOCK_RAW, 1)) < 0) { // Create socket, 1 == ICMP/
 perror("ping: creating a raw socket");
 exit(1);
 }
 pingaddr.sin_family = AF_INET; // Set domain
 if (!(h = gethostbyname(host))) { // get IP address
 fprintf(stderr, "ping: unknown host %s\n", host);
 exit(1);
 }
 memcpy(&pingaddr.sin_addr, h->h_addr,
sizeof(pingaddr.sin_addr)); //Set up host addr
 int hostname = h->h_name;
 pkt = (struct icmp *) packet;
 memset(pkt, 0, sizeof(packet));
 pkt->icmp_type = ICMP_ECHO; //Set ICMP type
 pkt->icmp_cksum = in_cksum((unsigned short *) pkt,
sizeof(packet));
 c = sendto(pingsock, packet, sizeof(packet), 0,
 (struct sockaddr *) &pingaddr, sizeof(struct sockaddr_in));
  while (1) {
 struct sockaddr_in from;
 size_t fromlen = sizeof(from);

 if ((c = recvfrom(pingsock, packet, sizeof(packet), 0,
 (struct sockaddr *) &from, &fromlen)) < 0) {
 if (errno == EINTR)
 continue;
 perror("ping: recvfrom");
 continue;
 }
 if (c >= 76) { /* ip + icmp */
 struct iphdr *iphdr = (struct iphdr *) packet;
 pkt = (struct icmp *) (packet + (iphdr->ihl << 2));
 /* skip ip hdr */
 if (pkt->icmp_type == ICMP_ECHOREPLY)
 break;
 }
 }
 printf("%s is alive!\n", hostname);
 return;
 int main ()
{
 ping ("www.google.com");
}