import os
from collections import OrderedDict
def generateDir(basedir):
    dir = OrderedDict()
    for root, dirs, files in os.walk(basedir):
        dir[root] = {'rel':root[len(basedir):], 'children':dirs, 'files':files}
    return dir