from textnode import TextNode
import os
import shutil

def main():
    path = 'static'
    print(get_dir(path))

def update_dir(path, new):
    if os.path.exists(path):
        shutil.rmtree(path)
    

def get_dir(path):
    fileLst = []
    dir = {}
    if os.path.exists(path):
        dirLst = os.listdir(path)
        for node in dirLst:
            if os.path.isfile(os.path.join(path, node)):
                fileLst.append(os.path.join(path, node))
            else:
                dir[os.path.join(path, node)] = get_dir(os.path.join(path, node))
        if dir != {}:
            dir[path] = fileLst
            return dir
        return fileLst
    raise ValueError(f'{path} does not exist')


    
    
main()