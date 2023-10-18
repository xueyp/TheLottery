import unittest
from thelottery import spider as spider


class TestSpider(unittest.TestCase):

    def test_getBallsByID(self):
        id = 2023002
        result = spider.getBallsByID(id)
        self.assertEqual(result, [2023002,2, 6, 10, 16, 18, 22, 13])


if __name__ == '__main__':

    unittest.main()
