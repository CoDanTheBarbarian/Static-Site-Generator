import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_child(self):
        node = HTMLNode(tag="tag", value="parent")
        self.assertIsInstance(node.children, list)

    def test_empty_props(self):
        node = HTMLNode(tag="tag", value="parent")
        self.assertIsInstance(node.props, dict)

    def test_props_to_html(self):
        node = HTMLNode(tag="tag", value="parent", props={"class": "container", "id": "kernel"})
        method_output = node.props_to_html()
        self.assertEqual(method_output, ' class="container" id="kernel"')
    

    def test_repr(self):
        child_node_1 = HTMLNode(tag="tag", value="child_1")
        child_node_2 = HTMLNode(tag="tag", value="child_2")
        node = HTMLNode(tag="tag", value="parent", children=[child_node_1, child_node_2], props={"class": "container", "id": "kernel"})
        node_text = repr(node)
        self.assertEqual(node_text, 
                         'HTMLNode(tag="tag", value="parent", children=[HTMLNode(tag="tag", value="child_1", children=[], props={}), HTMLNode(tag="tag", value="child_2", children=[], props={})], props= class="container" id="kernel")')


if __name__ == "__main__":
    unittest.main()