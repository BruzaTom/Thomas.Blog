import unittest
import re

from inline import split_nodes_delimiter, extract_markdown_links, extract_markdown_images, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode


node = TextNode('This is text with a **bold** word', 'bold')
node2 = TextNode('This is text with a *italic* word', 'italic')
node3 = TextNode('This is text with a `code` word', 'code')
node4 = TextNode('This is text with a secend `code` statement', 'code')

class Testsplit_nodes_delimiter(unittest.TestCase):
    def test_bold(self):
        #print('testing bold word...')
        new = split_nodes_delimiter([node], '**', node.text_type)
        #print(f'Results:{new}\n')

    def test_italic(self):
        #print('testing italic word...')
        new = split_nodes_delimiter([node2], '*', node2.text_type)
        #print(f'Results:{new}\n')

    def test_code(self):
        #print('testing code string...')
        new = split_nodes_delimiter([node3], '`', node3.text_type)
        #print(f'Results:{new}\n')

    def test_doubles(self):
        #print('testing 2 code nodes...')
        new = split_nodes_delimiter([node3, node4], '`', node3.text_type)
        #print(f'Results:{new}\n')

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        #print(f'\ntesting extract_markdown_images...\ntext:{text}\nresult:{extract_markdown_images(text)}')
        # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        #print(f'\ntesting extract_markdown_links...\ntext:{text}\nresult:{extract_markdown_links(text)}')
        # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

    def test_split_nodes_link(self):
        text2 = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        node2 = TextNode(text2, 'text',)
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = TextNode(
            text,
            'text',
        )
        new_nodes = split_nodes_link([node, node2])
        #print(f'\ntesting split_nodes_link...\ntext:{text}\ntext2:{text2}\nresult:{split_nodes_link([node, node2])}')

    def test_split_nodes_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        node = TextNode(text, 'text',)
        #print(f'\ntesting split_nodes_image...\ntext:{text}\nresult:{split_nodes_image([node])}')
        
    def test_text_to_textnodes(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        text2 = 'this is a [big link](www.wow.com) with a bigger ![image](fatfart.url)'
        #print(f'\ntesting text_to_textnodes...\ntext:{text}\nresult:{text_to_textnodes(text)}')



