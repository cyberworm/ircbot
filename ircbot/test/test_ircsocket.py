import socket
import unittest
from mock import Mock
from ircbot.ircsocket import IrcSocket
from ircbot.exceptions import TimeoutError


class TestIrcSocket(unittest.TestCase):
    def setUp(self):
        self.__socketMock = Mock(socket.socket())
        self.__ircSocket = IrcSocket(self.__socketMock)

    def tearDown(self):
        del self.__ircSocket
        del self.__socketMock

    def test_connect_should_call_connect_socket_method_with_server_and_port(self):
        server = 'irc.rizon.net'
        port = 6667
        self.__ircSocket.connect(server, port)
        self.__socketMock.connect.assert_called_once_with((server, port))

    def test_disconnect_should_call_close_socket_method(self):
        self.__ircSocket.disconnect()
        self.__socketMock.close.assert_called_once_with()

    def test_send_should_call_send_socket_method_with_content(self):
        self.__ircSocket.send('some content')
        self.__socketMock.send.assert_called_once_with('some content')

    def test_receive_should_call_recv_socket_method_and_return_received_content(self):
        expected = 'Hello World'
        self.__socketMock.recv.return_value = expected
        content = self.__ircSocket.receive()
        self.assertEqual(content, 'Hello World', 'Expected: %s, got: %s' % (expected, content))
        self.__socketMock.recv.assert_called_once_with(4096)

    def test_receive_should_call_recv_socket_method_and_raise_TimeoutError(self):
        expected = 'some timeout'
        self.__socketMock.recv.side_effect = socket.timeout('some timeout')

        try:
            self.__ircSocket.receive()
        except TimeoutError as timeout:
            self.assertEqual(timeout.message, expected, 'Expected: %s, got: %s' % (expected, timeout.message))

        self.__socketMock.recv.assert_called_once_with(4096)

    def test_set_timeout_should_call_set_timeout_socket_method_with_timeout_in_seconds(self):
        self.__ircSocket.set_timeout(300)
        self.__socketMock.settimeout.assert_called_once_with(300)


if __name__ == '__main__':
    unittest.main()
