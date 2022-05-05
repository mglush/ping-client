# PingClient.py

import sys
import time
import socket

# get the IP address and port number of the server,
# as inputted by the user during the call of this program.
serverName = sys.argv[1]
serverPort = int(sys.argv[2])

# create the UDP socket.
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# wait one second for a reply.
clientSocket.settimeout(1)

# message should be 64 bytes.
message = bytearray(64)
min_time = 2000
max_time = 0
total_time = 0
received = 0

for i in range(10):
    try:
        before = time.time() # start timer.
        # send the message.
        clientSocket.sendto(message, (serverName, serverPort))
        # listen for reply.
        data, server = clientSocket.recvfrom(2048)
        after = time.time() # end timer.

        # collect the min, max, and elapsed time.
        ping_time = after - before
        # keep track of the total time.
        total_time += ping_time
        if (ping_time < min_time):
            min_time = ping_time
        if (ping_time > max_time):
            max_time = ping_time
        
        received += 1

        # PRINT FORMAT
        # PING received from machine_name: seq#=X time=Y ms
        print("PING received from " + serverName + ": seq#=" + str(i + 1) + " time=" + str(ping_time) + " ms")
        time.sleep(1) # wait a second before the next request
    except socket.timeout as err:
        print("Request timeout for seq#=" + str(i + 1))

# PRINT FORMAT
# --- ping statistics ---
# X packets transmitted, Y received, Z% packet loss rtt min/avg/max = MIN AVG MAX ms
result = "10 packets transmitted, " + str(received) + " received, " + str(10*(10 - received)) + "% packet loss"
if received > 0:
    if min_time == 2000:
        min_time = 0
    average_time = total_time / 10
    min_time = round(min_time, 3)
    max_time = round(max_time, 3)
    average_time = round(average_time, 3)
    result += (" rtt min/avg/max = %0.3f %0.3f %0.3f ms" % (min_time, max_time, average_time))
print("--- ping statistics ---")
print(result)