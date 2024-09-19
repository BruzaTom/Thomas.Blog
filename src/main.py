from textnode import TextNode
import os
import shutil

def main():
    dir = get_dir('static')
    print(dir)

def update_dir(path, new):
    if os.path.exists(path):
        shutil.rmtree(path)
    

def get_dir(path):
    list = []
    if os.path.exists(path):
        copy = os.listdir(path)
        for node in copy:
            list.append(copy_to(os.path.join(path, node)))
        return list
    else:
        raise ValueError(f'{path} does not exist')

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
    
    
main()