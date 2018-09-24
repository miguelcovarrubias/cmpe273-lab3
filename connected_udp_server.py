
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class ConnectedHelloWorldServer(DatagramProtocol):
    def startProtocol(self):
        host = "127.0.0.1"
        port = 8001
        self.transport.connect(host, port)

    def datagramReceived(self, data, addr):
        print("[Server Side] Received the following message: %r from %s" % (data, addr))
        self.transport.write(data, addr)


reactor.listenUDP(8000, ConnectedHelloWorldServer())
reactor.run()

