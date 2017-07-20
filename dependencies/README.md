# Installed packages 

## DHCP and DNS

 * `sudo apt-get install isc-dhcp-server bind9` 

## FFMPEG/FFPLAY/FFSERVER
RPi uses a ARM CPU this means the software must be optimized "IN ORDER TO BE PROPERLY USED"

follow the walkthrough until you are ready to install ffmpeg:
 
* `https://trac.ffmpeg.org/wiki/CompilationGuide/RaspberryPi`

In the Raspberry , open a terminal and type this:

```
cd /usr/src
git clone git://source.ffmpeg.org/ffmpeg.git

cd ffmpeg
./configure
make && make install
```

##Install NGINX 

We need a webserver to serve the video on a Html page . To do so we use NGINX 
 * `sudo apt-get install ngnix`

#Install

