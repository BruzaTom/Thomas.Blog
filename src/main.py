from textnode import TextNode
import os
import shutil
from check_curuption import check_curr
from blocks import *

def main():
    path = 'static'

    #index2.md is moved to content and generates a index2.html file in public, then index2.html is placed in root and renamed index.html
    
    generate_pages_recursive('content', 'template.html', 'public')

def updateData(text, file):
    with open(file, "w") as f:
        f.write(text)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f'updating {dest_dir_path} with files in {dir_path_content} using {template_path}...')
    template = getText(template_path)
    content_tree = get_dir(dir_path_content)
    content_files = get_list(dir_path_content)
    files = []
    for file in content_files:
        files.extend(file)
    print(f'\t files grabbed:{files}')
    
    update_dir(dest_dir_path, content_tree, files)
    for i in range(0, len(files)):
        template = getText(template_path)
        md = getText(files[i])
        title = extract_title(files[i])
        html = markdown_to_html_node(md)
        htmlstring = html.to_html()
        html_page = getText(template_path).replace('{{ Title }}', title)
        html_page = html_page.replace('{{ Content }}', htmlstring)
        html_page = html_page.replace('<li></li>', '</li>')#bugg
        
        #formats for css classes
        html_page = use_nave(html_page)

        path = files[i].replace('md', 'html')
        md_to_html_path = path.replace(dir_path_content, dest_dir_path)
        print(f'\t\tupdating {md_to_html_path} with HTML generated from {files[i]}..')
        updateData(html_page, md_to_html_path)
        root_path = ''.join(md_to_html_path.split('/')[1:]) #remove  'public/' from public/index3.html
        text = getText(path.replace(dir_path_content, dest_dir_path))
        if os.path.exists(root_path): #else place from public
            updateData(text, root_path)
        else:
            raise Exception(f'there is no path {root_path} in root...')

def use_nave(script):
    # finds a list of links and edits script to use nave
    new = script.replace('<ul><li><a', '<nav class="navbar"><ul class="link-list"><li><a')
    return new.replace('</a></li></ul>', '</a></li></ul></nav>')

def getText(path):
    with open(path) as f:
        file_contents = f.read()
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
        shutil.copy2(files[t], os.path.join(path, node.replace('md', 'html')))
        t += 1
    

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