# Adaptative Livestream Script 

Imagine your network between the RPi and Smartphone has a huge packet loss/ RTT delay, this script can reduce the quality of 
the video in order to give you the possibility to see the video stream without lag but with lower quality.

[`Network status`](./Diagram.jpeg)


Supposing you are running the [`start_stream_gopro.py`](./start_stream_gopro.py) already, you should be able to receive the 
packets sent by the GoPro via `udp://:8554` 

Since you are receiving the `UDP packets` from the Go Pro, its time to Capture them and generate a videostream. To do this you 
will need to run this script: [`start_stream_ffmpeg.py`](./start_stream_ffmpeg.py)

To run this script you will need to open a new terminal and type this :
* `python2 start_stream_ffmpeg.py`


This script fetches the `stream of UDP data` using `FFmpeg` , changes it and sends it to whererever you may need the stream to 
be.In this case, I send it to the port 8090 of my raspberry.

The most important "feature" of this script, is the use of `FFmpeg` and `FFserver` to join the UDP packets and captured from 
the GO Pro and generating a videostream with them. You can then change the video format, the resolution,etc and you can 
also stream a modified version of the video to one or more devices.

## Script Functions

### Start FFserver 

This function, starts the FFserver in a background state, as it uses `nohup` . This allows the Python script to run 
while the FFserver and FFmpeg are launched. This also means that if for some reason the user logs out of the account 
the program will still be running. To stop/kill this process you will need to send a `SIGTERM` or `SIGKILL` signal to the process.

The configurations that can be used by this function are located [here](../Rpi_configs/ffserver_configs/)

### Start FFmpeg
This function starts the FFmpeg the same in the same way that FFserver is started.

It receives 3 inputs :
* quality, resolution of the video (ex: 720x480)
* streamin, location of the input stream(ex: udp://:8854)
* streamout, location of the output stream(ex: 127.0.0.1:8090/)

#### Warning 

When running these fucntions `nohup` process is launched. This means that the Pyhton Script forks a nohup process which will 
later fork a ffmpeg process. 
This little detail can cause you some headeaches, if you are not sure what is the PID of the process you want to be running in 
bakground.


### Kill process 

This function is used to kill the processes running in background by their PID. The processes can be `FFserver` or `FFmpeg` 
processes.

[Main Menu](../README.md)

