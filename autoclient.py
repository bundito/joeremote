from autobahn.asyncio.websocket import WebSocketClientProtocol, \
    WebSocketClientFactory

try:
    import asyncio
except ImportError:
    # Trollius >= 0.3 was renamed
    import trollius as asyncio


class MyClientProtocol(WebSocketClientProtocol):

    def onConnect(self, response):
        print("Server connected: {0}".format(response.peer))

    def onOpen(self):
        print("WebSocket connection open.")

        def hello():
            self.sendMessage(u"Hello, world!".encode('utf8'))
            self.sendMessage(b"\x00\x01\x03\x04", isBinary=True)
            self.factory.loop.call_later(1, hello)

        # start sending messages every second ..
        hello()

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            print("Text message received: {0}".format(payload.decode('utf8')))

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))


    def make_cxn(self):

        self.factory = WebSocketClientFactory(u"ws://10.0.0.135:10000")
        self.factory.protocol = MyClientProtocol

    def run_send_loop(self):

        loop = asyncio.get_event_loop()
        coro = loop.create_connection(self.factory, '10.0.0.135', 10000)
        loop.run_until_complete(coro)
        loop.run_forever()
        loop.close()