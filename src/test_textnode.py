import unittest

from textnode import TextNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)

    def test_is_diff(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "Bold", "https://www.boot.dev")
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_text_node_to_html(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("goggle", "link", "https://www.google.com")

        leaf = TextNode.text_node_to_html_node(node2)
        googlelink = leaf.to_html()
        self.assertEqual(googlelink, leaf.to_html())
        


if __name__ == "__main__":
    unittest.main()