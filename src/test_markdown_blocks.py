import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

def test_block_to_block_type(self):
    test_cases = [
        ("### This is a heading", "heading"),
        ("```This is code```", "code"),
        ("```This is two\nlines of code```", "code"),
        ("> This is a\n>multiple line\n>quote", "quote"),
        ("* This is an unordered list\n- with different markdown symbols", "unordered_list"),
        ("1. This is an ordered list\n2. That satisfies the conditions\n3. With three items", "ordered_list"),
        ("####### This is a non-heading (7 pound signs)\nthat should return 'paragraph'", "paragraph"),
        ("# Heading 1", "heading"),
        ("###### Heading 6", "heading"),
        ("1. Not an ordered list\n3. Because it doesn't increment properly", "paragraph")
    ]
    
    for block, expected_type in test_cases:
        with self.subTest(block=block):
            self.assertEqual(block_to_block_type(block), expected_type)


if __name__ == "__main__":
    unittest.main()
