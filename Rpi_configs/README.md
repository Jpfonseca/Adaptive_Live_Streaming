# Configuration

All the files mentioned in this file are available [here](../Rpi_configs/)

## DHCP Server Configuration

1. Configured the DHCP SERVER to give addresses to the new "machines in the network" in `/etc/dhcpd.conf`

2. Denied interfaces of `wlan0` (built-in Wifi module) in `/etc/dhcpcd.conf`

3. Configured the DHCP SERVER to serve requests on the interface `wlan0` in `/etc/default/isc-dhcp-server`


## Network configuration

1. In `/etc/network/interfaces` configured `wlan0` as:  
- Ip: 192.169.0.1 
- Netmask: 255.255.255.0
- Broadcast Address: 192.169.0.255
- Network: 192.169.0.0


2. Configured `wlan0` as an hotspot in `/etc/hostapd/hostapd.conf`

* WPA-PSK
* SSID:Saturday
* Passphrase:video12345

3. Set the path to the hostpad configuration in `/etc/default/hostapd`: 
 - DAEMON_CONF="/etc/hostapd/hostapd.conf"

## FFserver config 
1. Now we need to decide the configuration of the FFserver. To do this we need to create a file, where the configuration will 
be
set.
2. In the file we can configure the address and port where the stream will be streamed, the quality of it, the bandwidth 
available, the max number of clients, video resolution , etc.

There are several examples of configurations in the [`ffserver_configs/`](./ffserver_configs) folder.


[Main Menu](../README.md)|[Running some stuff](../scripts/Running.md)


