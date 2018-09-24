from __future__ import print_function

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastHelloWorldClient(DatagramProtocol):

    def startProtocol(self):
        # Join the multicast address, so we can receive replies:
        self.transport.joinGroup("228.0.0.5")
        # Send to 228.0.0.5:9999 - all listeners on the multicast address
        # (including us) will receive this message.
        message = b'Hello World'
        print("Sending message from client: %s" % message)
        self.transport.write(message, ("228.0.0.5", 9999))

    def datagramReceived(self, datagram, address):
        print("[Client Side] Datagram %s received from %s" % (repr(datagram), repr(address)))


reactor.listenMulticast(9999, MulticastHelloWorldClient(), listenMultiple=True)
reactor.run()
