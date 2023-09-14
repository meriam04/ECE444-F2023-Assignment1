from utils import utils
import unittest

class TestUtils(unittest.TestCase):
    util: utils
    
    def setUp(self):
        self.util = utils()

    def test_reversed_int(self):
        got = self.util.reversed(num = 1234)
        self.assertEqual(got, 4321)
        
    def test_reversed_float(self):
        got = self.util.reversed(num = 12.01)
        self.assertEqual(got, 21)
        got = self.util.reversed(num = 12.99999)
        self.assertEqual(got, 21)

    def test_reversed_str(self):
        got = self.util.reversed(num = '456')
        self.assertEqual(got, 654)
        
        # Error because cannot be converted to int
        with self.assertRaises(ValueError):
            self.assertRaises(self.util.reversed(num = '0x123'))

    def test_formatter_int(self):
        got = self.util.formatter(num = 36)
        self.assertEqual(got, ('0b100100','0o44'))
        

    def test_formatter_float(self):
        got = self.util.formatter(num = 36.0)
        self.assertEqual(got, ('0b100100','0o44'))
    
    def test_formatter_str(self):
        got = self.util.formatter(num = '36')
        self.assertEqual(got, ('0b100100','0o44'))
       
        # Error because cannot be converted to int
        with self.assertRaises(ValueError):
            self.assertRaises(self.util.reversed(num = '0x123'))

if __name__ == "__main__":
    unittest.main()
    