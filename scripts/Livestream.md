# Adaptative Livestream Script 

Imagine your network between the RPi and Smartphone has a huge packet loss/ RTT delay, this script can reduce the quality of 
the video in order to give you the possibility to see the video stream without lag but with lower quality.

Supposing you are running the [`start_stream_gopro.py`](./start_stream_gopro.py) already, you should be able to receive the 
packets sent by the GoPro via `udp://:8554` 

To run this script you will need to open a new terminal and type :
* `python2 start_stream_ffmpeg.py`


This script fetches the `stream of UDP data` using `FFmpeg` , changes it and sends it to whererever you may need the stream to 
be.In this case, I send it to the port 8090 of my raspberry.

The most important "feature" of this script, is the use of `FFmpeg` and `FFserver` to alter the videostream that comes from the 
`GoPro`. You can change the video format, the resolution,etc and you can stream this modified version of the video to one or 
more devices.

## Script Functions

### Start FFserver 

This function starts the ffserver in a background state, as it uses `nohup`. This allows the Python script to run while the 
FFserver is running. 
The configurations that can be used by this function are located [here](../Rpi_configs/ffserver_configs/)

### Start FFmpeg
This function starts the FFmpeg the same in the same way that FFserver is started.

It has receives 3 inputs :
* quality, resolution of the video (ex: 720x480)
* streamin, location of the input stream(ex: udp://:8854)
* streamout, location of the output stream(ex: 127.0.0.1:8090/)


### Kill process 

This function is used to kill the processes running in background by their PID. The processes can be FFserver or FFmpeg 
processes.

[Main Menu](../README.md)

