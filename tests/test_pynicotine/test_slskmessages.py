import unittest

from pynicotine.slskmessages import JustDecoded
from pynicotine.slskmessages import NetworkIntType
from pynicotine.slskmessages import NetworkLongLongType
from pynicotine.slskmessages import NetworkSignedIntType
from pynicotine.slskmessages import SlskMessage
from pynicotine.slskmessages import ToBeEncoded


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
