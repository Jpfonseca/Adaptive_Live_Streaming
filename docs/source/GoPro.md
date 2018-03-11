# Go Pro start Streaming

More information on using the Go Pro can be found [here](https://github.com/KonradIT/goprowifihack/)

To start receiving stream data from the Go Pro,  you must be connected to the wi-fi of the camera. You can check you connection   
by trying to access `10.5.5.9` on your browser. If a webpage with "links to the Go Pro folders" appears, you have successfully   
connected to the camera.

Now you want to obtain the `UDP stream` that the Go Pro transmists when in "livestreaming mode".

To do it you should run the program [src/scripts/start\_stream\_gopro.py](../../src/scripts/start_stream_gopro.py).

You can do it by opening a terminal on this folder and then run the following command:

* `python2 start_stream_gopro.py`

This Script starts the stream on the `Go Pro Hero 4 Black` version 05.00

## Warning

Although this program can be used to force streaming on the Go Pro, sometimes it is needed to restart the stream mannually . This can be done by reaching the following address \(while connected to the Go Pro's WIFI\):

* `'http://10.5.5.9:8080/gp/gpControl/execute?p1=gpStream&c1=restart'`

This program won't accept any inputs or outputs. After a few seconds it enters a infinite loop so when you need to kill it   
just press `Crtl^C`

[Main Menu](../README.md)\|[Adaptative Livestream](./Livestream.md)

