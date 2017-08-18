# Go Pro start Stream

Starts the stream on the Go Pro Hero 4 Black version 05.00

## start_stream_gopro.py

More information on using the Go Pro can be found [here](https://github.com/KonradIT/goprowifihack/)

### Warning
Although this program can be used to force streaming on the Go Pro, sometimes it is needed to restart the stream mannually . This can be done by reaching the 
following address (while connected to the Go Pro's WIFI):

* `'http://10.5.5.9:8080/gp/gpControl/execute?p1=gpStream&c1=restart'`

This program doesn't accept any inputs or outputs. After a few seconds it enters a infinite loop so when you need to kill it 
just press Crtl^C

[Main Menu](../README.md)|[Adaptative Livestream](./Livestream.md)|


