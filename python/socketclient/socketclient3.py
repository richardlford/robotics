import socket
import sys

#HOST, PORT = sys.argv[1], 9999
#HOST="rlfpi4a.local"
HOST=sys.argv[1]
PORT=9999

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    while True:
        print("Command?", end=" ")
        data=input()
        sock.sendall(bytes(data + "\n", "utf-8"))
        print("Sent:     {}".format(data))
        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
        print("Received: {}".format(received))
