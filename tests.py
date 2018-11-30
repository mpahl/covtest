import unittest

import code


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(code.smile(), ":)")


if __name__ == '__main__':
    unittest.main()
