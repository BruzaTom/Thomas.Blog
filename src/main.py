from textnode import TextNode
import os
import shutil
from check_curuption import check_curr
from blocks import *

def main():
    path = 'static'
    #print({'public': get_dir(path)},'\n')
    #print(get_list(path))
    files = []
    for file in get_list(path):
        files.extend(file)

    print(files)

    update_dir('public', get_dir(path), files)
    
    generate_page('static/content/index.md', 'template.html', 'public/content/index.html')

def generate_page(from_path, template_path, dest_path):
    print(f'generating page from {from_path}, to {dest_path}, using {template_path}')
    template = getText(template_path)
    md = getText(from_path)
    title = extract_title(from_path)
    html = markdown_to_html_node(md)
    htmlstring = html.to_html()
    print(htmlstring)

def getText(path):
    with open(path) as f:
        file_contents = f.read() #f.read() turns book text into long string
    return file_contents    

def extract_title(markdown):
    text = getText(markdown)    
    blocks = markdown_to_blocks(text)
    for block in blocks:
        if block_to_block_type(block) == 'h1':
            return strip(block)

def update_dir(path, tree, files):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    t=0
    for node in tree:
        if tree[node] == None:
            shutil.copy2(files[t], os.path.join(path, node))
            t += 1
            files = files[t:]
        else:
            update_dir(os.path.join(path, node), tree[node], files)
    

def get_dir(path):
    dir = {}
    if os.path.exists(path):
        dirLst = os.listdir(path)
        for node in dirLst:
            node_path = os.path.join(path, node)
            if os.path.isfile(node_path):
                dir[node_path.split('/')[-1]] = None
            else:
                dir[node_path.split('/')[-1]] = get_dir(node_path)
        return dir
    raise ValueError(f'{path} does not exist')


def get_list(path):
    list = []

    def copy_to(path):
        list = []
        dict = {}
        if os.path.isfile(path):
            return [path]
        copy = os.listdir(path)
        for node in copy:
            if os.path.isfile(os.path.join(path, node)):
                list.append(os.path.join(path, node))
            else:
                list.extend(copy_to(os.path.join(path, node)))
        return list

    if os.path.exists(path):
        copy = os.listdir(path)
        for node in copy:
            list.append(copy_to(os.path.join(path, node)))
        return list
    else:
        raise ValueError(f'{path} does not exist')
    



    
    
main()