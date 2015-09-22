import unittest
from ircbot.irccommands import IrcCommands


class TestIrcCommands(unittest.TestCase):
    def setUp(self):
        self.__ircCommands = IrcCommands()

    def tearDown(self):
        del self.__ircCommands

    def test_join_should_return_string_containing_join_command_with_channel_name(self):
        joincmd = 'JOIN #touhou-launcher\r\n'
        self.assertEqual(self.__ircCommands.join('touhou-launcher'), joincmd)

    def test_nick_should_return_string_containing_nick_command_with_nickname(self):
        nickcmd = 'NICK IrcBot\r\n'
        self.assertEqual(self.__ircCommands.nick('IrcBot'), nickcmd)

    def test_ping_should_return_string_containing_ping_command_with_server(self):
        pingcmd = 'PING irc.rizon.net\r\n'
        self.assertEqual(self.__ircCommands.ping('irc.rizon.net'), pingcmd)

    def test_pong_should_return_string_containing_pong_command_with_server(self):
        pongcmd = 'PONG irc.rizon.net\r\n'
        self.assertEqual(self.__ircCommands.pong('irc.rizon.net'), pongcmd)

    def test_priv_msg_should_return_string_containing_privmsg_command_with_target_and_message(self):
        msgcmd = 'PRIVMSG touhou-launcher :Hello World!\r\n'
        self.assertEqual(self.__ircCommands.privmsg('touhou-launcher', 'Hello World!'), msgcmd)

    def test_quit_should_return_string_containing_quit_command(self):
        quitcmd = 'QUIT\r\n'
        self.assertEqual(self.__ircCommands.quit(), quitcmd)

    def test_quit_should_return_string_containing_quit_command_with_a_message(self):
        quitcmd = 'QUIT :goodbye!\r\n'
        self.assertEqual(self.__ircCommands.quit('goodbye!'), quitcmd)

    def test_user_should_return_string_containing_user_command_with_nickname_and_server(self):
        nickname = 'IrcBot'
        server = 'irc.rizon.net'
        usercmd = 'USER %s %s %s :%s\r\n' % (nickname, server, server, nickname)
        self.assertEqual(self.__ircCommands.user(nickname, server), usercmd)


if __name__ == '__main__':
    unittest.main()
