#include <stdio.h>
  #include <stdlib.h>
  #include <sys/socket.h>
  #include <sys/types.h>
  #include <errno.h>
  #include <net/if.h>
  #include <sys/ioctl.h>
  //#include <linux/if_ether.h>
  #include <string.h>
 // #include <linux/in.h>
  
  int main(int argc, char **argv)
  {
    int sock, n;
    char buffer[2048];
    unsigned char *iphead, *ethhead;
    struct ifreq ethreq;
  
    if ( (sock=socket(PF_PACKET, SOCK_RAW,
                      htons(ETH_P_ALL)))<0) {
      perror("socket");
      exit(1);
    }
  
    /* Set the network card in promiscuos mode */
    strncpy(ethreq.ifr_name,"eth0",IFNAMSIZ);
    if (ioctl(sock,SIOCGIFFLAGS,&ethreq)==-1) {
      perror("ioctl");
      close(sock);
      exit(1);
    }
    ethreq.ifr_flags|=IFF_PROMISC;
    if (ioctl(sock,SIOCSIFFLAGS,&ethreq)==-1) {
      perror("ioctl");
      close(sock);
      exit(1);
    }
  
    while (1) {
      printf("----------\n");
      n = recvfrom(sock,buffer,2048,0,NULL,NULL);
  
      /* pkt processing done here and then sent
       * to the RANAP stack
       * */
  
      }
   return 0;
 }