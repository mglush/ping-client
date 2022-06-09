# UDP Ping Client Implementation in Python.
#### By Michael Glushchenko for UCSB CS176A Spring 2022 (Computer Networking).
###### Partners with Jack Rollinson.

## Purpose
  - Learn how clients and servers interract via socket programming.
  - Learn how the ping utility software works.
  - Model the ping utility server via a simple python program.

## How to Run
On one host:
~~~
python PingServer.py                      # start the server.
~~~
On another host:
~~~
python PingClient.py localhost 12000      # start the client.
~~~

## Functionality
1) The program sets up a server on localhost port 12000, and lets a client connect to it.\
2) The client sends 10 pings to the server, and waits exactly a second for reply.\
3) The server simulates artificial packet loss, and either sends a reply (with a 70% chance) or it doesn't.\
4) When the client receives a reply from the server, it records the round-trip time of the connection.\
5) If the client does not receive a reply from the server, it assumes the packet was lost, and sends a new ping request out.\
6) This goes on for a total of 10 times, at the end of which a linux-like ping message is printed, showing the average round-trip time, number of pings, percent of successfull pings, etc.
