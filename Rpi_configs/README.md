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

Setted the path to the hostpad configuration in `/etc/default/hostapd`: 
 - DAEMON_CONF="/etc/hostapd/hostapd.conf"


##FFserver config 

In the `etc/ffserver.conf` configured the address and port where the stream will be streamed, the quality of the stream, the bandwidth available, the max number of clients 

#Running the tools


##FFserver

Supposing you have 
