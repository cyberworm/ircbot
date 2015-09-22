class IrcSocket(object):
    def __init__(self, socket):
        self.__socket = socket

    def __del__(self):
        del self.__socket

    def connect(self, server, port):
        self.__socket.connect((server, port))

    def disconnect(self):
        self.__socket.close()

    def send(self, content):
        self.__socket.send(content)

    def receive(self):
        return self.__socket.recv(2048)
