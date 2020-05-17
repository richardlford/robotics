import socket
import sys

#HOST, PORT = sys.argv[1], 9999
HOST="rlfpi4a.local"
PORT=9999
data = " "
print("Default socket timeout is: {}".format(socket.getdefaulttimeout()))
def mysendreceive(data):
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))
        print("Sent:     {}".format(data))
        received = str(sock.recv(1024), "utf-8")
        print("Received: {}".format(received))
        return received
    
while True:
    print("Command?", end=" ")
    data=input()
    got = mysendreceive(data)
    print(got)