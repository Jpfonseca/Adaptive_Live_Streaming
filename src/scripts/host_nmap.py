#!/usr/bin/env python

import nmap # import nmap.py module
import os
import sys

def host_discovery(network):
    nm = nmap.PortScanner() #starts Nmap
    print '----------------------------------------------------'

    nm.scan(hosts=network, arguments='-n -sP -PE -PA21,23,80,3389') #performs a scan in a specified network.
                                                                    #looks from hosts with ports 21,23,80,3389 open

    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]# list of hosts with open ports

    print "List of Hosts\n"
    print "-1) Exit"
    i=1

    for host, status in hosts_list:
        string =str(i)+"){"+ str(host) + "}:{" + str(status)+ "}" #prints the network  and the status(up or down)
        print (string)
        i=i+1

    kb=-1
    while(kb<1 or kb>i):
        kb=raw_input("Which is the host that will receive the stream ?")
        kb=int(kb)
        if kb==-1:
            print "Ending"
            sys.exit()
    return hosts_list[int(kb-1)][0] #let's you choose the host you want to connect with
                                    #returns that host address

if __name__ == "__main__":
    #In case you want to run this script solo
    host=host_discovery('192.168.0.0/24') #Network I used to test this script
    print host
    sys.exit()
