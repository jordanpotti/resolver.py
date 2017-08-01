import socket
import sys

if len(sys.argv) != 2:
        print "Usage: resolver.py <list of hostnames>"
        sys.exit(0)
s = set()
with open(sys.argv[1],"r") as text:
        for line in text:
                if ('abcdefghijklmnopqrstuvwxyz') not in line:
                        resolved = socket.getfqdn(line)
                        print resolved
                else:
                        resolved = socket.gethostbyname(line.strip())
                        print resolved
                        with open(sys.argv[1]+".txt","a") as resolved_list:
                                resolved_list.write(resolved+"\n")
