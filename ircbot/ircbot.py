class IrcBot(object):
    def __init__(self, ircsocket, irccommands):
        self.__ircsocket = ircsocket
        self.__irccommands = irccommands
        self.__nickname = None

    def __del__(self):
        del self.__ircsocket
        del self.__irccommands
        del self.__nickname

    def connect(self, server, port):
        self.__ircsocket.connect(server, port)
        self.__ircsocket.send(self.__irccommands.nick(self.__nickname))
        self.__ircsocket.send(self.__irccommands.user(self.__nickname, server))

    def disconnect(self):
        self.__ircsocket.send(self.__irccommands.quit())
        self.__ircsocket.disconnect()

    def join(self, channel):
        self.__ircsocket.send(self.__irccommands.join(channel))

    def pong(self, data):
        self.__ircsocket.send(self.__irccommands.pong(data))

    def receive(self, timeout=300):
        self.__ircsocket.set_timeout(timeout)
        return self.__ircsocket.receive()

    def say(self, target, message):
        self.__ircsocket.send(self.__irccommands.privmsg(target, message))

    def __set_nickname(self, nickname):
        self.__nickname = nickname

    def __get_nickname(self):
        return self.__nickname

    nickname = property(__get_nickname, __set_nickname)
