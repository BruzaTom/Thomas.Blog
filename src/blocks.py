
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
        return 'heading 1'
    if block[:3] == '## ':
        return 'heading 2'
    if block[:4] == '### ':
        return 'heading3'
    if block[:5] == '#### ':
        return 'heading 4'
    if block[:6] == '##### ':
        return 'heading 5'
    if block[:7] == '###### ':
        return 'heading 6'
    if (block[:3] == '```') & (block[len(block)-3:] == '```'):
        return 'code block'
    if (block[0] == '>'):
        lines = block.split('\n')
        for string in lines:
            if string[0] != '>':
                return 'failed quote block'
        return 'quote block'
    if (block[0] == '*'):
        lines = block.split('\n')
        for string in lines:
            if string[0] != '*':
                return 'failed unordered list'
        return 'unordered list'
    if (block[0] == '-'):
        lines = block.split('\n')
        for string in lines:
            if string[0] != '-':
                return 'failed unordered list'
        return 'unordered list'
    if (block[:3] == '1. '):
        lines = block.split('\n')
        for t in range(0, len(lines)):
            if lines[t][:3] != f'{t+1}. ':
                return 'failed ordered list'
        return 'ordered list'
    return 'normal paragraph'
    
def getText(path):
    with open(path) as f:
        file_contents = f.read() #f.read() turns book text into long string
    return file_contents
path = 'md.md'
text = getText(path)
blocks = markdown_to_blocks(text)
blocktypes = []
for block in blocks:
    blocktypes.append(block_to_block_type(block))