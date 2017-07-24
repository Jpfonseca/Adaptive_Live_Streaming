#!/usr/bin/python
import sys
import os
import time
import signal
import math

##files in the /scripts/ folder
from connect_status import check_connection
from host_nmap import host_discovery

def process_num(process):
    return os.system("pidof " + process)

def start ffserver()
# change process to whatever command you may need to execute
    process ="sudo ffserver -d -f /etc/ffserver.conf"
    os.system("nohup "+process+" &")
    return process

def start_ffmpeg(quality, streamin, streamout):
# change process to whatever command you may need to execute
    process ="ffmpeg bbb_1080.mp4"
    os.system("nohup "+process+" &")
    return process

def kill_process(process):
    pid=process_num(process)

    if pid!=0 :
        print "Problem while fetching process {PIDOF exit code :"+str(pid)+"}"
        return 0
    os.system("nohup "+"kill "+process+" &")
    return 1

def start_streaming(streamin, streamout, manual_stop):
    quality=['1','2','3']
    i=0

    process_ffserver =start_ffserver()

    process_ffmpeg =start_ffmpeg(quality[i],streamin,streamout)

    status_prob=0

    while(1):
        status=check_connection("10",streamout)
        if math.fabs(status) ==1:

            if status ==-1 :
                print "Can't Stream video . Lost connection to the network\n Status Problem: "+str(status_prob)+"\n"
                if status_prob==2 :
                    return 1

                ++status_prob

            if kill_process(process_ffmpeg)==0:
                return 1

            time.sleep(3)

            ++i
            if i<=len(quality):
                print "Testing new quality \n"
                status_prob=0
                process =start_ffmpeg(quality[i],streamin,streamout)
            else:
                print "Tested all qualities . Your network may have some issues\n"
                kill_process(process_ffserver)                
                return 2
        else :

            if manual_stop==1:

                print "Stop Stream ?? \n 0)YES \n Other)NO \n"
                testVar = raw_input()

                if int(testVar)==0 :
                    print "Stream Ending \n"
                    kill_process(process_ffmpeg)
                    kill_process(process_ffserver)
                    return 0

    return 0


if __name__ == "__main__":

# I have configured the network 192.169.0.0/24 on the RPI
# as the network that will be used as a wifi Access Point

    network='192.168.0.0/24'
    host=host_discovery(network)


#Ending Stream Manually
    print "Do you wish to end the stream manually (without Ctrl^C) \n 0) NO \n Others) Yes"

    manual_stop_stream=raw_input()
    print "\n"
    if int(manual_stop_stream)!=0:
        manual_stop_stream=1


##stream  input & output
    var=start_streaming("15", host,manual_stop_stream)
    print "Exited with code " +str(var)
    sys.exit()
