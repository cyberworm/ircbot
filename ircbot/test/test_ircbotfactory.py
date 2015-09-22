import unittest
from ircbot.ircbot import IrcBot
from ircbot.ircbotfactory import IrcBotFactory


class TestFactory(unittest.TestCase):
    def setUp(self):
        self.__ircbotfactory = IrcBotFactory()

    def tearDown(self):
        del self.__ircbotfactory

    def test_create_should_return_instance_of_ircbot(self):
        self.assertIsInstance(self.__ircbotfactory.create(), IrcBot)


if __name__ == '__main__':
    unittest.main()
