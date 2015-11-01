import unittest
from mock import Mock
from mock import call
from ircbot.ircsocket import IrcSocket
from ircbot.irccommands import IrcCommands
from ircbot.ircbot import IrcBot


class TestIrcBot(unittest.TestCase):
    def setUp(self):
        self.__ircSocketMock = Mock(IrcSocket(None))
        self.__ircCommandsMock = Mock(IrcCommands())
        self.__ircBot = IrcBot(self.__ircSocketMock, self.__ircCommandsMock)

    def tearDown(self):
        del self.__ircSocketMock
        del self.__ircCommandsMock
        del self.__ircBot

    def test_get_set_nickname_via_property(self):
        nickname = 'IrcBot'
        self.__ircBot.nickname = 'IrcBot'
        self.assertEqual(self.__ircBot.nickname, nickname)

    def test_connect_should_call_connect_ircsocket_method_with_server_and_port_and_send_nick_and_user_message(self):
        server = 'irc.rizon.net'
        port = 6667
        nickname = 'IrcBot'
        nickcmd = 'NICK %s\r\n' % nickname
        usercmd = 'USER %s %s %s :%s\r\n' % (nickname, server, server, nickname)
        calls = [call(nickcmd), call(usercmd)]

        self.__ircCommandsMock.nick.return_value = nickcmd
        self.__ircCommandsMock.user.return_value = usercmd

        self.__ircBot.nickname = nickname
        self.__ircBot.connect(server, port)

        self.__ircCommandsMock.nick.assert_called_once_with(nickname)
        self.__ircCommandsMock.user.assert_called_once_with(nickname, server)
        self.__ircSocketMock.connect.assert_called_once_with(server, port)
        self.__ircSocketMock.send.assert_has_calls(calls)

    def test_disconnect_should_call_disconnect_ircsocket_method(self):
        quitcmd = 'QUIT\r\n'

        self.__ircCommandsMock.quit.return_value = quitcmd

        self.__ircBot.disconnect()

        self.__ircCommandsMock.quit.assert_called_once_with()
        self.__ircSocketMock.send.assert_called_once_with(quitcmd)
        self.__ircSocketMock.disconnect.assert_called_once_with()

    def test_join_should_call_send_ircsocket_method_with_join_command(self):
        joincmd = 'JOIN touhou-launcher\r\n'
        self.__ircCommandsMock.join.return_value = joincmd

        self.__ircBot.join('touhou-launcher')

        self.__ircCommandsMock.join.assert_called_once_with('touhou-launcher')
        self.__ircSocketMock.send.assert_called_once_with(joincmd)

    def test_pong_should_call_send_ircsocket_method_with_pong_command(self):
        pongcmd = 'PONG abcdef\r\n'
        self.__ircCommandsMock.pong.return_value = pongcmd

        self.__ircBot.pong('abcdef')

        self.__ircCommandsMock.pong.assert_called_once_with('abcdef')
        self.__ircSocketMock.send.assert_called_once_with(pongcmd)

    def test_receive_should_call_receive_ircsocket_method(self):
        expected = 'Hello World'
        self.__ircSocketMock.receive.return_value = expected
        content = self.__ircBot.receive()
        self.assertEqual(content, 'Hello World', 'Expected: %s, got: %s' % (expected, content))
        self.__ircSocketMock.receive.assert_called_once_with()

    def test_say_should_call_send_ircsocket_method_with_privmsg_command(self):
        msgcmd = 'PRIVMSG touhou-launcher :Hello World!\r\n'

        self.__ircCommandsMock.privmsg.return_value = msgcmd

        self.__ircBot.say('touhou-launcher', 'Hello World!')

        self.__ircCommandsMock.privmsg.assert_called_once_with('touhou-launcher', 'Hello World!')
        self.__ircSocketMock.send.assert_called_once_with(msgcmd)


if __name__ == '__main__':
    unittest.main()
