#!/usr/bin/python
import sys
import json
import socket
import requests
from time import sleep


def get_command_msg(id):
    return "_GPHD_:%u:%u:%d:%1lf\n" % (0, 0, 2, 0)


if __name__ == "__main__":
#Go Pro Livestream start link
# http://10.5.5.9/gp/gpExec?p1=gpStreamA9&c1=restart

    uri_status='http://10.5.5.9:8080/gp/gpControl/execute?p1=gpStream&c1=restart'
    req=requests.get(uri_status)

#Try to send the signal to start the stream
    if req.status_code != 200:
        print"Cannot connect to Go Pro" + "\n" +"Check connection-manager"
        sys.exit()
    else:

# Keep stream Alive python script from:
#https://gist.github.com/3v1n0/38bcd4f7f0cb3c279bad#file-hero4-udp-keep-alive-send-py
#as on 20 July 2017 22:48
        UDP_IP = "10.5.5.9"
        UDP_PORT = 8554
        KEEP_ALIVE_PERIOD = 2500
        KEEP_ALIVE_CMD = 2
        MESSAGE = get_command_msg(KEEP_ALIVE_CMD)

        print("UDP target IP:", UDP_IP)
        print("UDP target port:", UDP_PORT)
        print("message:", MESSAGE)

        if sys.version_info.major >= 3:
            MESSAGE = bytes(MESSAGE, "utf-8")

        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
            sleep(KEEP_ALIVE_PERIOD/1000)
