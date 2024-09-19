from textnode import TextNode
import os
import shutil

def main():
    path = 'static'
    #print({'public': get_dir(path)},'\n')
    #print(get_list(path))
    files = []
    for file in get_list(path):
        files.extend(file)

    #print(files)

    update_dir(path, 'public', get_dir(path), files)
    




def update_dir(old_path, path, tree, files):
    if os.path.exists(path):
        shutil.rmtree(path)
    def make_dir(path, tree, files):
        os.mkdir(path)
        t = 0
        for node in tree:
            if tree[node] == None:
                shutil.copy(files[t], os.path.join(path, node))
                t += 1
                files = files[t:]
            else:
                make_dir(os.path.join(path, node), tree[node], files)
    for node in tree:
        make_dir(path, tree, files)
    

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