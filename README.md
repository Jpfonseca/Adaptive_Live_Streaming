# Adaptative Livestreaming

This project aims to provide a easy configurable way to livestream a video and adapt the stream to the changes in the network.
This means that when the bandwidth available decreases/increases, the quality of the video should follow the same behaviour.

## Architecture

The early version of this project begun with a streaming data from a device(Go Pro) to another device (Cellphone), 
while 
avoiding to have a laggy stream.

The stream provided by the Go Pro can be directly viewed on the cellphone using the Go Pro App, but the cellphone cannot share 
the video to other devices. This means we need a device to capture the stream and to distribute it to other devices.

To capture the image/video from the Go Pro I used a Raspberry Pi , which is also used to send the data to the Cellphone.

Below is a overview of the devices used and their function:
![Overview](./images/arch_top.jpeg)

The Stream from the Go Pro comes via `UDP` in `MPEG-TS` and browsers don't like this format,  we need to transcode the 
video to another format, supported by browsers. This work is done by `FFmpeg` and `FFserver` which provide a simple way to 
transcode video, while it is still being captured. 

In this project, this type of transcoding, delays continue to grow while video is being captured.

Below is a simple scheme of the process :
![Scheme](./images/arch.jpeg)






