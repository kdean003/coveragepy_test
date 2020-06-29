import unittest
from example import getCondition

class MyTest(unittest.TestCase):
    def test_TrueCond(self):
        self.assertEqual(getCondition(True), True)

    def test_FalseCond(self):
        self.assertEqual(getCondition(False), False)
