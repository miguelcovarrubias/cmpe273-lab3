# cmpe273-lab3


## Multicast example run
### Server
```
miguel.covarrubias$ python connected_udp_server.py
[Server Side] Received the following message: b'Hello World' from ('127.0.0.1', 8001)
```
### Client
```
miguel.covarrubias$ python connected_udp_client.py
[Client Side] We can only send to host 127.0.0.1 port 8000
Message to send b'Hello World':
received b'Hello World' from ('127.0.0.1', 8000)
```

## Multicast example run
### Server
```miguel.covarrubias$ python multicast_udp_server.py
Datagram b'Hello World' received from ('10.77.154.239', 9999)
Datagram b'Server: Hello World' received from ('10.77.154.239', 9999)
```
### Client
```
miguel.covarrubias$ python multicast_udp_client.py
Sending message from client: b'Hello World'
[Client Side] Datagram b'Hello World' received from ('10.77.154.239', 9999)
```