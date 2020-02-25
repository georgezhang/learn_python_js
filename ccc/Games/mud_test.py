import unittest
from mud import start_game

class MudTestCase(unittest.TestCase):
    def test_start_game(self):
        self.assertEqual(start_game(), True)


if __name__ == '__main__':
    unittest.main()
