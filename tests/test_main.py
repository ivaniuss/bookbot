import unittest

from src.main import get_content, count_words
class TestGetContent(unittest.TestCase):
    def test_get_content(self):
        content = get_content('./books/frankenstein.txt')
        self.assertTrue(isinstance(content, str))
        self.assertGreater(len(content), 0)

    def test_count_words(self):
        content = get_content('./books/frankenstein.txt')
        words = count_words(content)
        self.assertGreater(len(words), 0)

if __name__ == '__main__':
    unittest.main()