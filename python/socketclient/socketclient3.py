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
    ok = True
    while ok:
        print("Command?", end=" ")
        try:
            data=input()
            try:
                sock.sendall(bytes(data + "\n", "utf-8"))
            except:
                print("Send error")
                ok = False
                
                
            if ok:
                print("Sent:     {}".format(data))
                # Receive data from the server and shut down
                try:
                    received = str(sock.recv(1024), "utf-8")
                    if received == "":
                        print("receive error (got nothing), assume server went away")
                        ok = False
                    else:
                        print("Received: {}".format(received))
                except:
                    print("receive error")
        except EOFError:
            print("Exiting")
            ok = False