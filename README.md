# UDP Ping Client Implementation in Python.
#### By Jack (John) Rollinson and Michael Glushchenko for UCSB CS176A Spring 2022 (Computer Networking).

1) The program sets up a client and server on port numbers inputted by the user.\
2) The client then sends 10 pings to the server, and waits exactly a second for reply.\
3) The server simulates artificial packet loss, and either sends a reply or doesn't.\
4) When the client receives a reply from the server, it records the round-trip time of the connection.\
5) If the client does not receive a reply from the server, it assumes the packet was lost, and sends a new ping out.\
6) This goes on for a total of 10 times, at the end of which a linux-like ping message is printed, showing the average round-trip time, number of pings, percent of successfull pings, etc.
