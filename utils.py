import os
from collections import OrderedDict
from itertools import chain
from conf import conf
def generateDir(basedir):
    dir = OrderedDict()
    for root, dirs, files in os.walk(basedir):
        dir[root] = {'rel':root[len(basedir):], 'children':dirs, 'files':files}
    return dir

class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.files = []
    def __repr__(self):
        return self.name
    def add_child(self, child):
        self.children.append(child)
    
    def add_file(self, file):
        self.files.append(file)
        
    def add_children(self, children):
        self.children.extend(children)
    
    def add_files(self, files):
        self.files.extend(files)
    
    def children(self):
        return len(self.children)
    
    def files(self):
        return len(self.files)
def add(dir, rel, files, level):
    for f in dir:
        if isinstance(f, list):
            continue
        if f.name == rel[-2]:
            folder = Folder(rel[level+1])
            folder.add_files(files)
            f.add_child(folder)
            return
    add(list(chain.from_iterable([f.children for f in dir])), rel, files, level+1)
        
def generateList(basedir):
    dir = []
    for path, children, files in os.walk(basedir):
        if path == basedir:
            continue
        
        rel = path[len(basedir):].split(conf['SEP'])
        if len(rel) == 1:
            folder = Folder(rel[0])
            folder.add_files(files)
            dir.append(folder)
        else:
            add(dir, rel, files, 0)
    return dir
if __name__ == '__main__':
    for f in generateList('/media/pi/Seagate Backup Plus Drive1/'):
        print(f, f.children, [f2.children for f2 in f.children])