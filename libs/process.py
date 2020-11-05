from pathlib import Path
from itertools import islice
import os

def sortFileByTime():
    dirpath = '../CEWIS/out/'
    path = sorted(Path(dirpath).iterdir(), key=os.path.getmtime)
    res = list(islice(reversed(path), 0, 4))
    res.reverse()
    return res

def getFileName(res):
    mylist = []
    for x in res:
        filename = os.path.basename(x)
        mylist.append(filename)
    return mylist