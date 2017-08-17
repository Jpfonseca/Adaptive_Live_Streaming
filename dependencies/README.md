# Package Dependencies

In order to use the project you will need to install the following packages on your Raspberry:

* DHCP and DNS
* FFmpeg/FFplay/FFserver
* Ngnix
* Nmap


## DHCP and DNS

 * `sudo apt-get install isc-dhcp-server bind9` 

## FFMPEG/FFPLAY/FFSERVER
RPi uses a ARM CPU(there are different versions of arm, rpi 2 and rpi 3 use different versions of arm) this means the software 
must be optimized to the specific architecture. 
`IN ORDER TO BE PROPERLY USED` follow the walkthrough until you are ready to install ffmpeg:


* `https://trac.ffmpeg.org/wiki/CompilationGuide/RaspberryPi`

OR

* `https://owenashurst.com/?p=242&p=242`

## Install NGINX 

We need a webserver to serve the video on a Html page . To do so we use NGINX 
 * `sudo apt-get install ngnix`

## Install NMAP
We need to know the ip of the device which will "receive the stream"(smartphone).
I have decided that device will be on the network `192.169.0.1` and the mask is `255.255.255.0`
 * `sudo apt-get install nmap`



<br/>
We now have all the packages needed to run the project

[Main Menu](../README.md)|[Next](./Python.md)

