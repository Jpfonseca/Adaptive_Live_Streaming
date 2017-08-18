# Adaptative Livestream Script 

## start_stream_ffmpeg.py
Imagine your network between the RPi and Smartphone has a huge packet loss/ RTT delay, this script can reduce the quality of 
the video in order to give you the possibility to see the video stream without lag but with lower quality.

Supposing you are running the `start_stream_gopro.py` already, you should be able to receive the packets send by the GoPro via `udp://:8554`. 
Therefore this script fetches the stream of UDP data using FFmpeg , changes it and sends it to whererever you may need the stream to be(I send it to the port 
8090).

The most important "feature" of this script, is how the FFmpeg can alter the videostream that comes from the GoPro.


[Main Menu](../README.md)

