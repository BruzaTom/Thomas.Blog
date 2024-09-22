from textnode import TextNode
import os
import shutil
from check_curuption import check_curr
from blocks import *

def main():
    path = 'static'
    #print({'public': get_dir(path)},'\n')
    #print(get_list(path))
    
    #generate_page('content/index.md', 'template.html', 'public/index.html')
    generate_pages_recursive('content', 'template.html', 'public')

def updateData(text, file):
    with open(file, "w") as f:
        f.write(text)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    template = getText(template_path)
    content_tree = get_dir(dir_path_content)
    static_tree = get_dir('static')
    static_tree.update(content_tree)
    static_files = get_list('static')
    content_files = get_list(dir_path_content)
    static_files.extend(content_files)
    files = []
    for file in static_files:
        files.extend(file)
    
    update_dir(dest_dir_path, static_tree, files)
    content_paths = []
    for file in content_files:
        content_paths.extend(file)
    for i in range(0, len(content_paths)):
        template = getText(template_path)
        md = getText(content_paths[i])
        title = extract_title(content_paths[i])
        html = markdown_to_html_node(md)
        htmlstring = html.to_html()
        html_page = getText(template_path).replace('{{ Title }}', title)
        html_page = html_page.replace('{{ Content }}', htmlstring)
        path = content_paths[i].replace('md', 'html')
        updateData(html_page, path.replace(dir_path_content, dest_dir_path))

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
    print(tree)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
    t=0
    for node in tree:
        if tree[node] == None:
            if (t+1) > len(files):
                shutil.copy2('md.md', os.path.join(path, node))
            if node[len(node)-2:] == 'md':
                shutil.copy2(files[t], os.path.join(path, node.replace('md', 'html')))
                t += 1
                files = files[t:]
            else:
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