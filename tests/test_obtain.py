import unittest
import sys, os

sys.path.insert(0, os.path.abspath("src"))
from thelottery import obtain as obtain


class TestObtain(unittest.TestCase):
    def test_ObtainOne(self):
        result = obtain.obtainOne(2023001)
        self.assertEqual(result, [2023001, 9, 16, 18, 22, 28, 32, 2])


"""
    def test_ObtainRange(self):
        result = obtain.obtainRange(2023001, 2023010)
        self.assertNotEqual(obtain.balls, None)

    def test_ObtainByYear(self):
        results = obtain.obtainByYear(2023)
        self.assertNotEqual(obtain.balls, None)
"""

if __name__ == "__main__":
    unittest.main()
