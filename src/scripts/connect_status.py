#!/usr/bin/python

import os
import subprocess
import re
import sys


#Supposing there is a device connected to the raspberry
#we need to check if the Raspberry can reach it
#and the quality of the connection(round trip delay)

#In both functions the  information is obtained from a 
#ping output, to determined network


def subprocessping(npings, url):
    proc = subprocess.Popen(["ping","-c", str(npings), url],stdout=subprocess.PIPE)
    proc.wait()
    return proc.communicate()


# Average Round Trip Time Delay
def check_rtt(npings, url):
    (out,err) =subprocessping(npings,url)

    print out

    if out.find("packet")==-1:
        print "Cannot reach  " +url
        return -1

    stringlist=out.split("/")
    rtt=float(stringlist[4]) #avg rtt

    if rtt>=10:
        return 1
    else :
        if rtt<5:
            return 0
        else:
            return 2



# Packet loss 
def check_connection(npings, url):
    (out,err) =subprocessping(npings,url)

    print out
    if out.find("packet")==-1:
        print "Cannot reach  " +url
        return -1

    stringlist=out.split(",")
    string=stringlist[2].split() #string[2] ="0% packet loss"
    packetloss=[int(s) for s in string[0].split() if s.isdigit()]

    if packetloss>=50:
        return 1
    else :
        if packetloss[2]!=0:
            return 0
        else:
            return 2


if __name__ == "__main__":
    address="google.pt"
    npings=10
    print "Packet loss: "+str(check_connection(npings, address))+"\n Round Trip Delay: "+str(check_connection(npings, 
address))
    sys.exit()

