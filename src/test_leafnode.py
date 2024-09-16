import unittest

from leafnode import LeafNode

node = LeafNode('a', 'link', {"href": "https://www.google.com", 
    "target": "_blank"})

node2 = LeafNode('a', 'link', {"href": "https://www.google.com", 
    "target": "_blank"})

node3 = LeafNode('i', 'italic text.')

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(node, node2)

    def test__children_none(self):
        self.assertIsNone(node.children)

    def test_is_diff(self):
        self.assertNotEqual(node3.tag, node2.tag)

    def test_to_html(self):
        print(f'node3.to_html:{node2.to_html()}')
