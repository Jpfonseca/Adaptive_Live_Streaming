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



# Python libraries Dependencies

In this project I have used `Python 2.7` therefore all libraries should be compatible with this version:

## Install Python-nmap
We need to install pip to use  external libraries such as requests. We can do this by running:
 * `sudo apt-get install python2-nmap`


## Install Python-pip

We need to install pip to use  external libraries such as requests. We can do this by running:
 * `sudo apt-get install python2-pip`


### Install packages using pip

We need to install some packages for further use in python . We can do it by running :

 * `sudo pip2 install -r requirements.txt`



We now have all the needed packages and libraries needed to run the project, so we can start configuring some stuff.

[Main Menu](../README.md)|[Next](../Rpi_Configs/README.md)

