import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):

    def test_extract_title(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""
        title = extract_title(md)
        self.assertEqual(title, "this is an h1")

    def test_extract_title_error(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""
        with self.assertRaises(ValueError):
            extract_title(md)
