import unittest

from textnode import TextNode, text_type_bold, text_type_code, text_type_image, text_type_italic, text_type_link, text_type_text


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_italic)
        self.assertNotEqual(node, node2)
    
    def test_url_eq(self):
        node = TextNode("This is a text node", text_type_bold, "https://bottdev.com")
        node2 = TextNode("This is a text node", text_type_bold, "https://bottdev.com")
        self.assertEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", text_type_bold, "https://bottdev.com")
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_text_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is another text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()