# Sample python server that accepts commands over a socket and executes them.
# This version first tries to evaluate the command as an expression and if
# that succeeds reports the result. If that fails then it is executed as a
# statement in the global scope. If that also fails an error message is given.
import socketserver
import socket
import sys

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# Sample utility function. Any added at this scope will be available.
def myadd(x, y):
    return x + y

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
external_ip = get_ip()

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        try:
            decoded = self.data.decode("utf-8")
            print("decoded = {}".format(decoded))
            
            # First try to evaluate as expression.
            try:
                raw_output = eval(decoded)
                print("raw_output = {}".format(raw_output))
                result = str(raw_output)
                print("result = {}".format(result))
            except:
                # Execute as statement.
                
                # Note: Addeding globals() as the second argument executes the
                # command in the global scope, so that variables values are kept.
                exec(decoded, globals())
                result = "Executed: {}".format(decoded)
        except:
            result = "Unexpected error: {}".format(sys.exc_info())
        print(result)
        resultbytes = bytes(result + "\n", "utf-8")
        print("resultbytes = {}".format(resultbytes))
        # just send back the same data, but upper-cased
        self.request.sendall(resultbytes)


if __name__ == "__main__":
    HOST, PORT = external_ip, 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
