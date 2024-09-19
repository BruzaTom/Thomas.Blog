from textnode import TextNode
import os
import shutil

def main():
    path = 'static'
    print({'public': get_dir(path)},'\n')
    print(get_list(path))



def update_dir(path, tree):
    if os.path.exists(path):
        shutil.rmtree(path)
    for node in tree:
        if tree[node] != None:
            os.mkdir(node)
    

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