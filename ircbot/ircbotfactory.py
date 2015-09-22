import socket
from ircbot import IrcBot
from irccommands import IrcCommands
from ircsocket import IrcSocket


class IrcBotFactory(object):
    def create(self):
        return IrcBot(IrcSocket(socket.socket()), IrcCommands())
