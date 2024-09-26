from htmlnode import HTMLNode
from parentnode import ParentNode
from textnode import TextNode
from leafnode import LeafNode
from inline import *

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    for i in range(0, len(blocks)):
        if blocks[i][0] == ' ':
            blocks[i] = blocks[i][1:]
        if blocks[i][-1] == ' ':
            blocks[i] = blocks[i][:len(blocks[i])-1]  
    return blocks

def block_to_block_type(block):
    if block[:2] == '# ':
        return 'h1'
    if block[:3] == '## ':
        return 'h2'
    if block[:4] == '### ':
        return 'h3'
    if block[:5] == '#### ':
        return 'h4'
    if block[:6] == '##### ':
        return 'h5'
    if block[:7] == '###### ':
        return 'h6'
    if (block[:3] == '```') & (block[len(block)-3:] == '```'):
        return 'pre'#for <pre><code></code><pre>
    if (block[:2] == '> '):
        lines = block.split('\n')
        for string in lines:
            if string[:2] != '> ':
                return 'failed quote block'
        return 'blockquote'
    if (block[:2] == '* '):
        lines = block.split('\n')
        for string in lines:
            if string[:2] != '* ':
                print('failed ul')
                return 'ul'
        return 'ul'
    if (block[:2] == '- '):
        lines = block.split('\n')
        for string in lines:
            if string[:2] != '- ':
                print('failed ul')
                return 'ul'
        return 'ul'
    if (block[:3] == '1. '):
        lines = block.split('\n')
        for t in range(0, len(lines)):
            if lines[t][:3] != f'{t+1}. ':
                print('failed ol')
                return 'ol'
        return 'ol'
    return 'p'

def text_to_children(text):#the text has not been stripped of ````
    if block_to_block_type(text) == 'pre':
        text = strip(text)
        return [TextNode(f'{text}', 'code')]
    else:
        return text_to_textnodes(text)
    
def strip(block):
    if block[:2] == '# ':
        return block[2:]
    if block[:3] == '## ':
        return block[3:]
    if block[:4] == '### ':
        return block[4:]
    if block[:5] == '#### ':
        return block[5:]
    if block[:6] == '##### ':
        return block[6:]
    if block[:7] == '###### ':
        return block[7:]
    if (block[:2] == '> '):
        return block.replace('> ', '')
    if (block[:2] == '* '):
        block = block.replace('* ', '')
        lines = block.split('\n')
        for i in range(0, len(lines)):
            lines[i] = f'<li>{lines[i]}</li>'
        return '\n'.join(lines)
    if (block[:2] == '- '):
        block = block.replace('- ', '')
        lines = block.split('\n')
        for i in range(0, len(lines)):
            lines[i] = f'<li>{lines[i]}</li>'
        return '\n'.join(lines)
    if (block[:3] == '1. '):
        lines = block.split('\n')
        for t in range(0, len(lines)):
            lines[t] = f'<li>{lines[t][3:]}</li>'
        return '\n'.join(lines) 
    if (block[:3] == '```') & (block[len(block)-3:] == '```'):
        return block[3:len(block)-3:]
    return block
    

def markdown_to_html_node(markdown):
    blocks =  markdown_to_blocks(markdown)
    blocktypes = []
    parentNodes = []
    for block in blocks:
        blocktypes.append(block_to_block_type(block))
    for i in range(0, len(blocks)):
        if blocktypes[i] != 'pre':
            blocks[i] = strip(blocks[i])
        #print(blocks[i])       #debug 
        parentNodes.append(ParentNode(f'{blocktypes[i]}', text_to_children(blocks[i])))
    return ParentNode(tag='div', children=parentNodes)

def getText(path):
    with open(path) as f:
        file_contents = f.read() 
    return file_contents