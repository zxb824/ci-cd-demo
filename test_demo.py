import unittest
from demo import add

class TestAdd(unittest.TestCase):
    def test_add_success(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
