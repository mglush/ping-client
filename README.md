# UDP Ping Utility Implementation in Python.
#### By Michael Glushchenko for UCSB CS176A Spring 2022 (Computer Networking).
###### Partners with Jack Rollinson.

## Table of Contents
* [Purpose](https://github.com/mglush/ping-utility/blob/main/README.md#purpose)
* [Installation](https://github.com/mglush/ping-utility/blob/main/README.md#installation)
* [How To Run](https://github.com/mglush/ping-utility/blob/main/README.md#how-to-run)
* [Functionality](https://github.com/mglush/ping-utility/blob/main/README.md#functionality)
* [Sample Output](https://github.com/mglush/ping-utility/blob/main/README.md#sample-output)

## Purpose
  - Learn how clients and servers interract via socket programming.
  - Learn how the ping utility software works.
  - Model the ping utility server via a simple python program.

## Installation
~~~
git clone git@github.com:mglush/ping-client.git   # clone repository.
cd ping-client                                    # enter repository folder.
~~~

## How to Run
On one host:
~~~
python PingServer.py                      # start the server.
~~~
On another host:
~~~
python PingClient.py 0.0.0.0 12000        # start the client.
~~~

## Functionality
1) The program sets up a server on localhost port 12000, and lets a client connect to it.\
2) The client sends 10 pings to the server, and waits exactly a second for reply.\
3) The server simulates artificial packet loss, and either sends a reply (with a 70% chance) or it doesn't.\
4) When the client receives a reply from the server, it records the round-trip time of the connection.\
5) If the client does not receive a reply from the server, it assumes the packet was lost, and sends a new ping request out.\
6) This goes on for a total of 10 times, at the end of which a linux-like ping message is printed, showing the average round-trip time, number of pings, percent of successfull pings, etc.

## Sample Output
<img width="640" alt="Screen Shot 2022-06-08 at 6 15 57 PM" src="https://user-images.githubusercontent.com/59711300/172743586-e723a0a2-ab87-456a-9e25-4171e2f1f013.png">
