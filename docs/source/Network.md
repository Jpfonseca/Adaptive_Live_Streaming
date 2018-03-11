# Network Scripts

## connect\_status.py

Checks if the connection to some IP address  has a significant packet loss or if the round trip time is higher than expected.

### Inputs

* npings , number of pings\(ex: 10\)
* url, Ip address/ URL of Website\(ex: google.com\)

### Outputs

#### Packet Loss

* -1, in case the IP address is not reachable
* 0 , if the connection has a packet losses &lt; 50%
* 1 , if the connection has a packet losses &gt; 50%
* 2 , if the connection has no packet lost

#### Round Trip Time delay\(ms\)

* -1, in case the IP address is not reachable
* 0 , if the connection RTT &lt;5 ms
* 1 , if the connection RTT &gt;=10 ms
* 2 , if the connection   5&lt;RTT&lt;10 ms

## host\_nmap.py

Lists the devices found on a specific network

### Inputs

* network \(ex: '127.0.0.0/24'\)    Be sure you specified the network mask !

### Outputs

The list of hosts in a determined network and the option for you to select one of them.  
This option will help to determine which device will receive the streamed video.

[Main Menu](../README.md)

