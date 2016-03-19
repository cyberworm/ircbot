from exceptions import TimeoutError
from socket import timeout


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

    def receive(self, size=4096):
        try:
            return self.__socket.recv(size)
        except timeout as e:
            raise TimeoutError(e.message)

    def set_timeout(self, seconds):
        self.__socket.settimeout(seconds)
