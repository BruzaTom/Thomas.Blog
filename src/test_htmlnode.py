import unittest

from htmlnode import HTMLNode

node = HTMLNode('a', 'link', props = {"href": "https://www.google.com", 
    "target": "_blank"})

node2 = HTMLNode('a', 'link', props = {"href": "https://www.google.com", 
    "target": "_blank"})

node3 = HTMLNode('h1', 'Welcome to My Website', props = {"class": "main-heading", 
    "id": "page-title"})

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(node, node2)

    def test__children_none(self):
        self.assertIsNone(node.children)

    def test_is_diff(self):
        self.assertNotEqual(node3.tag, node2.tag)

    def test_props_to_html(self):
        print(f'node3.props_to_html:{node3.props_to_html()}')
