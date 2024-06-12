import unittest

from src.main import get_content

class TestGetContent(unittest.TestCase):
    def test_get_content(self):
        content = get_content('./books/frankenstein.txt')
        self.assertTrue(isinstance(content, str))
        self.assertGreater(len(content), 0)

if __name__ == '__main__':
    unittest.main()