import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(tag="tag", value="parent", props={"class": "container", "id": "kernel"})
        method_output = node.props_to_html()
        self.assertEqual(method_output, ' class="container" id="kernel"')
    

    def test_values(self):
        node = HTMLNode("tag", "parent")
        
        self.assertEqual(node.tag, "tag")
        self.assertEqual(node.value, "parent")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node = HTMLNode("tag", "parent", None, props={"class": "container", "id": "kernel"})
        node_2 = HTMLNode("tag", "parent", ['child_1', 'child_2'], None)
        
        self.assertEqual(repr(node), "HTMLNode(tag, parent, children: None, {'class': 'container', 'id': 'kernel'})")
        self.assertEqual(repr(node_2), "HTMLNode(tag, parent, children: ['child_1', 'child_2'], None)")

if __name__ == "__main__":
    unittest.main()