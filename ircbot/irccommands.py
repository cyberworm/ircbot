class IrcCommands(object):
    COM_JOIN = 'JOIN'
    COM_NICK = 'NICK'
    COM_PING = 'PING'
    COM_PONG = 'PONG'
    COM_PRIVMSG = 'PRIVMSG'
    COM_QUIT = 'QUIT'
    COM_USER = 'USER'

    def join(self, channel):
        return self.COM_JOIN + ' #%s\r\n' % channel

    def nick(self, nickname):
        return self.COM_NICK + ' %s\r\n' % nickname

    def ping(self, server):
        return self.COM_PING + ' %s\r\n' % server

    def pong(self, data):
        return self.COM_PONG + ' %s\r\n' % data

    def privmsg(self, target, message):
        return self.COM_PRIVMSG + ' %s :%s\r\n' % (target, message)

    def quit(self, message=None):
        return self.COM_QUIT + ' :%s\r\n' % message if message else self.COM_QUIT + '\r\n'

    def user(self, nickname, server):
        return self.COM_USER + ' %s %s %s :%s\r\n' % (nickname, server, server, nickname)
