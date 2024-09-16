import unittest

from leafnode import LeafNode
from parentnode import ParentNode

node = LeafNode('a', 'link', {"href": "https://www.google.com", 
    "target": "_blank"})

node2 = LeafNode('a', 'link', {"href": "https://www.google.com", 
    "target": "_blank"})

node3 = LeafNode('i', 'italic text.')

item1 = LeafNode('li', 'apple')
item2 = LeafNode('li', 'bananna')
item3 = LeafNode('li', 'cake')

googlelink = LeafNode('a', 'google', {"href": "https://www.google.com", 
    "target": "_blank"})

text = LeafNode(None, f'here is a link to {googlelink.to_html()}. looks good.')

parent = ParentNode('p', [text])
parent2 = ParentNode('blockquote', [parent,])

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(node, node2)

    def test__children_none(self):
        self.assertIsNone(node.children)

    def test_is_diff(self):
        self.assertNotEqual(node3.tag, node2.tag)

    def test_to_html(self):
        print(f'parent.to_html:{parent.to_html()}')
        print(f'parent2.to_html:{parent2.to_html()}')
