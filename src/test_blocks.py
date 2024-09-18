import unittest
from blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node

def getText(path):
    with open(path) as f:
        file_contents = f.read() #f.read() turns book text into long string
    return file_contents
path = 'md.md'
text = getText(path)


class Test_blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = getText(path)
        #print(f'\ntesting markdown_to_blocks...\ntext:\n{text}\nresult:\n{markdown_to_blocks(text)}')

    def test_block_to_block_type(self):
        blocks = markdown_to_blocks(text)
        blocktypes = []
        for block in blocks:
            blocktypes.append(block_to_block_type(block))
        #print(f'\ntesting block_to_block_type...\ntext:\n{text}\nresult:\n{blocktypes}')

    def test_markdown_to_html_node(self):
        print(f'\ntesting markdown_to_html_node...\ntext:\n{text}\nresult:\n{markdown_to_html_node(text)}')