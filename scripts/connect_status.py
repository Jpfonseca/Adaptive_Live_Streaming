#!/usr/bin/python

import os
import subprocess
import re
import sys


def subprocessping(npings, url):
    proc = subprocess.Popen(["ping","-c", npings, url],stdout=subprocess.PIPE)
    proc.wait()
    return proc.communicate()



##Supposing there is a device connected to the raspberry
##we need to check if the rasp can reach it
##and the quality of the connection(round trip delay)
##
##In both functions the  information is obtained from a 
##ping output to determined network

## Average Round Trip Time Delay
def check_rtt(npings, url):
    (out,err) =subprocessping(npings,url)

    #print out

    if out.find("packet")==-1:
        print "Cannot reach  " +url
        return -1


    strings1=out.split("/")
    values1=[]


    for i in range(3, 7):
        values1.append(int(re.search(r'\d+', strings1[i]).group()))

    #Round Trip delay info (ms)
    if values1[1]>=10:
        return 1
    else :
        if values1[1]<5:
            return 0
        else:
            return 2



## Packet loss 
def check_connection(npings, url):
    (out,err) =subprocessping(npings,url)

    #print out
    if out.find("packet")==-1:
        print "Cannot reach  " +url
        return -1

    strings=out.split(",")
    values=[]

    for i in range(0, len(strings)):
        values.append(int(re.search(r'\d+', strings[i]).group()))

    #Percentage of lost packets
    if values[2]>=50:
        return 1
    else :
        if values[2]!=0:
            return 0
        else:
            return 2

if __name__ == "__main__":

    var=check_connection("10", "google.pt")
    var1= check_rtt("10", "google.pt")
    print "Packet loss: "+str(var)+"\n Round Trip Delay: "+str(var1)
    sys.exit()
