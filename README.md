# Adaptative Livestreaming


## Architecture

This project aims to provide a easy configurable way to livestream a video and adapt the stream to the changes in the network.
This means that when the bandwidth available decreases/increases, the quality of the video should follow the same behaviour.

The early version of this project begun with a streaming data from a device(Go Pro) to another device(Cellphone), while 
avoiding to have a laggy stream.
To capture the image/video from the GoPro I used a Raspberry Pi , which is also used to send the data to the Cellphone.

![Architecture](./images/arch_top.jpeg)

