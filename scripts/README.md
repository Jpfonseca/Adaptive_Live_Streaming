# Python Scripts

## connect_status.py

Checks if the connection to some IP address  has significant packet loss

### Inputs

* npings , number of pings
* url, Ip address/ URL of Website

### Outputs
* -1, in case the IP address is not reachable
* 0 , if the connection has a packet losses < 50%
* 1 , if the connection has a packet losses > 50%
* 2 , if the connection has no packet lost


## start_stream_gopro.py

Starts the stream on the Go Pro Hero 4 Black version 05.00

More information on using the Go Pro can be found [here](https://github.com/KonradIT/goprowifihack/)

### Warning
Although this program can be used to force streaming on the Go Pro, sometimes it is needed to restart the stream mannually . This can be done by reaching the 
following address (while connected to the Go Pro's WIFI):

* `'http://10.5.5.9:8080/gp/gpControl/execute?p1=gpStream&c1=restart'`


## start_stream_ffmpeg.py
Imagine your network between the RPi(PC) and cellphone has a huge packet loss, this script can reduce the quality of the video in order to give you the 
possibility to see the video stream without lag.

Supposing you are running the `start_stream_gopro.py` already, you should be able to receive the packets send by the GoPro via `udp://:8554`. 
Therefore this script fetches the stream of UDP data using FFmpeg , changes it and sends it to whererever you may need the stream to be(I send it to the port 
8081).
The most important "feature" of this script, is how the FFmpeg can alter the videostream that comes from the GoPro.

