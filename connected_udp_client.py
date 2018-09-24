
from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class ConnectedHelloWorldClient(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"
        port = 8000
        message = b"Hello World"
        self.transport.connect(host, port)
        print(("[Client Side] We can only send to host %s port %d" % (host, port)))
        print("Message to send %s:" % message)
        self.transport.write(message)


    def datagramReceived(self, data, addr):
        print("received %r from %s" % (data, addr))

    def connectionRefused(self):
        print("No one listening")

# 0 means any port, we don't care in this case
reactor.listenUDP(8001, ConnectedHelloWorldClient())
reactor.run()
