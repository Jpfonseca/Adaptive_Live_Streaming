#!/usr/bin/python
import sys
import os
import time
import signal
import math

##files in the /scripts/ folder
from connect_status import check_connection
from connect_status import check_rtt

from host_nmap import host_discovery

def process_num(process):
    return os.system("pidof " + process)

def start_ffserver():
    # change process to whatever command you may need to execute

    process ="ffserver -d -f ../Rpi_configs/ffserver_mjpg.conf"      # These .conf files have the configuration of
    #process ="ffserver -d -f ../Rpi_configs/ffserver_webm.conf"     #  the video sent to the phone

    os.system("nohup "+process+" &")
    return process

def start_ffmpeg(quality, streamin, streamout):
# change process to whatever command you may need to execute

#Type of Input stream:

#1) Video from GoPro/Computer
    #ffmpeg -benchmark -re -i http://10.5.5.9:8080/videos/DCIM/100GOPRO/GOPR0675.MP4 -tune zerolatency -probesize 8192 -s 1920x1080  -c copy -vcodec libx264 http://127.0.0.1:8090/feed1.ffm

#2) Livestream from GoPro
    #ffmpeg -an -fflags nobuffer -f:v mpegts -probesize 8192 -i udp://:8554 -s 480x360  http://127.0.0.1:8090/feed1.ffm
    process ="ffmpeg -an -fflags nobuffer -f:v mpegts -tune zerolatency -probesize 8192 -i "+streamin+" -s "+quality+" "+streamout
    os.system("nohup "+process+" &")
    #print process 
    return process

def kill_process(process):
    pid=process_num(process)

    if pid!=0 :
        print "Problem while fetching process {PIDOF exit code :"+str(pid)+"}"
        return 0
    return 1

def start_streaming(npings,destinationhost,streamin, streamout, manual_stop,data_collection):
#Stream video resolution

    quality=["1920x1080","1280x720","1024x768","800x600","720x480","480x360"]
    i=0

    process_ffserver =start_ffserver()

    process_ffmpeg =start_ffmpeg(quality[i],streamin,streamout)

    while(1):

        status=check_rtt(npings,destinationhost)

        if math.fabs(status) ==1:
            if kill_process("ffmpeg")==0:
                return 1
            ##data_collection is 1 when the stream is not delay tolerant
            if data_collection==1:
                kill_process("ffserver")
                time.sleep(3)
                #os.system("nohup "+"sudo rm -rf /tmp/feed1.ffm"+" &")           
                process_ffserver =start_ffserver()

            i=i+1
            if i<len(quality):
                print "Testing new quality \n"
                process =start_ffmpeg(quality[i],streamin,streamout)
            else:
                print "Tested all qualities . Your network may have some issues\n"
                kill_process("ffserver")                
                kill_process("ffmpeg")
                return 2
        else :

            if manual_stop==1:

                print "Stop Stream ?? \n 0)YES \n Other)NO \n"
                testVar = raw_input()

                if int(testVar)==0 :
                    print "Stream Ending \n"
                    kill_process("ffserver")
                    kill_process("ffmpeg")
                    return 0

    return 0


if __name__ == "__main__":

# I have configured the network 192.169.0.0/24 on the RPI
# as the network that will be used as a wifi Access Point

    network='192.169.0.0/24'
    destinationhost=host_discovery(network)


#Ending Stream Manually
    print "Do you want to stream with delay tolerance or livestream with image loss?? \n 0) Delay tolerant streaming \n Others) Livestream with image loss\n"

    data_collection=raw_input()
    print "\n"
    if int(data_collection)!=0:
        data_collection=1


    print "Do you wish to end the stream manually (without Ctrl^C) \n 0) NO \n Others) Yes\n"

    manual_stop_stream=raw_input()
    print "\n"
    if int(manual_stop_stream)!=0:
        manual_stop_stream=1
    

    streamin="udp://:8554"
    streamout="http://127.0.0.1:8090/feed1.ffm"
##stream  input & output
    var=start_streaming("10", destinationhost, streamin ,streamout,manual_stop_stream,data_collection)
    kill_process("ffserver")
    print "Exited with code " +str(var)
    sys.exit()
