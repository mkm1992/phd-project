traceroute
==========

Simple traceroute program made as exercise for computer networks course. Works atop of ICMP protocol and makes use of raw sockets - therefore requires root privileges.

It generally acts exactly the same way as standard `traceroute` command with `-I` flag. Mine version is somehow faster and better (obviously). No DNS lookup, though.

Code is written in pure C with heavy use of Unix specific libraries. Because of that I *had* to use ugly unix-style convention of creating meaningless abbreviations like `recvmtr` instead of `recive_multiple_traceroute`. Do not kill me for this.

Running
-------
Program is very simple and works well with `clang` and `gcc` compilers. Just `make` to build it.

Basic execution:

    sudo ./traceroute 8.8.8.8
    sudo ./traceroute -t 5000 8.8.8.8
    sudo ./traceroute -m 5 8.8.8.8

For more info check:

    ./traceroute --help
