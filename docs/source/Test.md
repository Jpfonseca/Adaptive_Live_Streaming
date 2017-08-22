# Access the Stream

Supposing you kept the same configs for your raspberry, your smartphone needs to be connected to the "Saturday 
Network" (Raspberry hotspot).

When you are connected, open your smartphone's browser and try to access the ip `192.169.0.1`. If everything went well you must 
be seing a webpage with a  webplayer in it. Then depending on the address of the stream your player may be showing something.

To change the source of the stream edit the  `line 33` of the [src/Website/index.html](../../src/Website/index.html) file.


If you want to see the stream on the browser, without the player, you can head to `192.169.0.1/stream<insert stream type>`, 
where the available stream types can be :`mjpg` or `webm`. Choose the correct one, accordingly to your FFserver 
[Configuration](../Configuration/README.md)
.


[Main Menu](../README.md)

