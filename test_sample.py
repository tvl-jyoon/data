import pytest
import unittest

class Test(unittest.TestCase):
    def testSum(self):
        self.assertEqual(1+1,2)


if __name__ == '__main__':
    unittest.main()
