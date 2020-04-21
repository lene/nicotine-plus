import unittest

from pynicotine.slskmessages import AddUser
from pynicotine.slskmessages import ChangePassword
from pynicotine.slskmessages import GetPeerAddress
from pynicotine.slskmessages import GetUserStatus
from pynicotine.slskmessages import JustDecoded
from pynicotine.slskmessages import Login
from pynicotine.slskmessages import NetworkIntType
from pynicotine.slskmessages import NetworkLongLongType
from pynicotine.slskmessages import NetworkSignedIntType
from pynicotine.slskmessages import NotifyPrivileges
from pynicotine.slskmessages import RemoveUser
from pynicotine.slskmessages import SetStatus
from pynicotine.slskmessages import SetWaitPort
from pynicotine.slskmessages import SlskMessage
from pynicotine.slskmessages import ToBeEncoded
from pynicotine.slskmessages import Unknown6


class ToBeEncodedTest(unittest.TestCase):
    def test_all(self):
        # Arrange
        string, encoding = 'teststring', 'latin'

        # Act
        obj = ToBeEncoded(string, encoding)

        # Assert
        self.assertEqual(b'teststring', obj.bytes)
        with self.assertRaises(AttributeError):
            obj.bytes = 'teststring'
        self.assertEqual('i', obj[7])
        self.assertEqual("b'teststring'", str(obj))
        self.assertEqual("ToBeEncoded(b'teststring', latin)", obj.__repr__())


class JustDecodedTest(unittest.TestCase):
    def test_all(self):
        # Arrange
        bytes_, encoding = b'testbytes', 'utf-8'

        # Act
        obj = JustDecoded(bytes_, encoding)

        # Assert
        self.assertEqual('testbytes', obj.str)
        self.assertEqual('e', obj[7])
        self.assertEqual("b'testbytes'", str(obj))
        self.assertEqual("JustDecoded(b'testbytes', utf-8)", obj.__repr__())

    def test_set(self):
        # Arrange
        bytes_, encoding = b'testbytes', 'utf-8'

        # Act
        obj = JustDecoded(bytes_, encoding)
        obj.str = 'testanotherstring'

        # Assert
        self.assertEqual('testanotherstring', obj.str)
        self.assertEqual('t', obj[7])
        self.assertEqual("b'testbytes'", str(obj))
        self.assertEqual("JustDecoded(b'testbytes', utf-8)", obj.__repr__())


class SlskMessageTest(unittest.TestCase):
    def test_packObject(self):
        # Arrange
        obj = SlskMessage()

        # Act
        int_message = obj.packObject(123)
        long_int_message = obj.packObject(123123123123)
        bytes_message = obj.packObject(b'testbytes')
        to_be_encoded_message = obj.packObject(ToBeEncoded('teststring', 'utf-8'))
        str_message = obj.packObject('teststring')
        net_int_message = obj.packObject(NetworkIntType(123))
        net_signed_int_message = obj.packObject(NetworkSignedIntType(123))
        net_long_long_message = obj.packObject(NetworkLongLongType(123))

        # Assert
        self.assertEqual(b'{\x00\x00\x00', int_message)
        self.assertEqual(b'\xb3\xc3\xb5\xaa\x1c\x00\x00\x00', long_int_message)
        self.assertEqual(b'\t\x00\x00\x00testbytes', bytes_message)
        self.assertEqual(b'\n\x00\x00\x00teststring', to_be_encoded_message)
        self.assertEqual(b'\n\x00\x00\x00teststring', str_message)
        self.assertEqual(b'{\x00\x00\x00', net_int_message)
        self.assertEqual(b'{\x00\x00\x00', net_signed_int_message)
        self.assertEqual(b'{\x00\x00\x00\x00\x00\x00\x00', net_long_long_message)


class LoginMessageTest(unittest.TestCase):
    def test_makeNetworkMessage(self):
        # Arrange
        obj = Login(username='test', passwd='s33cr3t', version=157)

        # Act
        message = obj.makeNetworkMessage()

        # Assert
        self.assertEqual(
            b'\x04\x00\x00\x00test\x07\x00\x00\x00s33cr3t\x9d\x00\x00\x00 \x00\x00\x00d'
            b'bc93f24d8f3f109deed23c3e2f8b74c\x11\x00\x00\x00',
            message)


class ChangePasswordMessageTest(unittest.TestCase):
    def test_makeNetworkMessage(self):
        # Arrange
        obj = ChangePassword(password='s33cr3t')

        # Act
        message = obj.makeNetworkMessage()

        # Assert
        self.assertEqual(
            b'\x07\x00\x00\x00s33cr3t',
            message)


class SetWaitPortMessageTest(unittest.TestCase):
    def test_makeNetworkMessage(self):
        # Arrange
        obj = SetWaitPort(port=1337)

        # Act
        message = obj.makeNetworkMessage()

        # Assert
        self.assertEqual(
            b'9\x05\x00\x00',
            message)


class GetPeerAddressMessageTest(unittest.TestCase):
    def test_makeNetworkMessage(self):
        # Arrange
        obj = GetPeerAddress(user='test')

        # Act
        message = obj.makeNetworkMessage()

        # Assert
        self.assertEqual(
            b'\x04\x00\x00\x00test',
            message)


class AddUserMessageTest(unittest.TestCase):
    def test_makeNetworkMessage(self):
        # Arrange
        obj = AddUser(user='test')

        # Act
        message = obj.makeNetworkMessage()

        # Assert
        self.assertEqual(
            b'\x04\x00\x00\x00test',
            message)


class Unknown6MessageTest(unittest.TestCase):
    def test_makeNetworkMessage(self):
        # Arrange
        obj = Unknown6(user='test')

        # Act
        message = obj.makeNetworkMessage()

        # Assert
        self.assertEqual(
            b'\x04\x00\x00\x00test',
            message)


class RemoveUserMessageTest(unittest.TestCase):
    def test_makeNetworkMessage(self):
        # Arrange
        obj = RemoveUser(user='test')

        # Act
        message = obj.makeNetworkMessage()

        # Assert
        self.assertEqual(
            b'\x04\x00\x00\x00test',
            message)


class GetUserStatusMessageTest(unittest.TestCase):
    def test_makeNetworkMessage(self):
        # Arrange
        obj = GetUserStatus(user='test')

        # Act
        message = obj.makeNetworkMessage()

        # Assert
        self.assertEqual(
            b'\x04\x00\x00\x00test',
            message)


class SetStatusMessageTest(unittest.TestCase):
    def test_makeNetworkMessage(self):
        # Arrange
        obj = SetStatus(status=1)

        # Act
        message = obj.makeNetworkMessage()

        # Assert
        self.assertEqual(
            b'\x01\x00\x00\x00',
            message)


class NotifyPrivilegesMessageTest(unittest.TestCase):
    def test_makeNetworkMessage(self):
        # Arrange
        obj = NotifyPrivileges(token=123456, user='test')

        # Act
        message = obj.makeNetworkMessage()

        # Assert
        self.assertEqual(
            b'@\xe2\x01\x00\x04\x00\x00\x00test',
            message)
