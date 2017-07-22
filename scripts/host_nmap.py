#!/usr/bin/env python

import nmap # import nmap.py module
import os
import sys

def host_discovery(network):
    nm = nmap.PortScanner() 
    print '----------------------------------------------------'

    nm.scan(hosts=network, arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

    print "List of Hosts\n"
    print "-1) Exit"
    i=1

    for host, status in hosts_list:
        string =str(i)+"){"+ str(host) + "}:{" + str(status)+ "}"
        print (string)
        i=i+1

    kb=-1
    while(kb<1 or kb>i):
        kb=raw_input("Which is the host that will receive the stream ?")
        kb=int(kb)
        if kb==-1:
            print "Ending"
            sys.exit()
    return hosts_list[int(kb-1)][0]

if __name__ == "__main__":
    host=host_discovery('192.168.0.0/24')
    print host
    sys.exit()
