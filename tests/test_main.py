import unittest
from src.main import soma

class TestMain(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(3, 5), 8)
if __name__ == '__main__':
    unittest.main()