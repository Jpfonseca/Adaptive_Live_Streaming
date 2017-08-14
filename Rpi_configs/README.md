# Configuration

## DHCP Server Configuration

Configured the DHCP SERVER to give addresses to the new "machines in the network" in `dhcpd.conf`

Denied interfaces of `wlan0` (built-in Wifi module) in `/etc/dhcpcd.conf`

Configured the DHCP SERVER to serve requests on the interface `wlan0` in `/etc/default/isc-dhcp-server`


## Network configuration

In `/etc/network/interfaces` configured `wlan0`:  
- Ip: 192.169.0.1 
- Netmask: 255.255.255.0
- Broadcast Address: 192.169.0.255
- Network: 192.169.0.0

Configured `wlan0` as an hotspot in `/etc/hostapd/hostapd.conf`

WPA-PSK
SSID:Saturday
Passphrase:video12345

Set the path to the hostpad configuration in `/etc/default/hostapd`: 
 - DAEMON_CONF="/etc/hostapd/hostapd.conf"

## FFserver config 
Now we need to decide the configuration of the FFserver. To do this we need to create a file, where the configuration will be
set.
In the file we can configure the address and port where the stream will be streamed, the quality of it, the bandwidth 
available, the max number of clients, video resolution , etc.

There are several examples of configurations in the `ffserver_configs/` folder.


# Running the tools	


## FFserver

Supposing you have  installed the FFmpeg with all extra packages, you will be able to stream every type of video you want.
Furthermore, you will have the possibility to change the quality of the stream/video and manipulating the output. This means,
that you decide the format of the stream.



