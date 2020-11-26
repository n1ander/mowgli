from pathlib import Path
from itertools import islice
import os
import glob

def sortFileByTime():
    path = glob.glob('../CEWIS/out/*.csv')
    path.sort(key=os.path.getctime)
    res = list(islice(reversed(path), 0, 4))
    return res

def getFileName(res):
    mylist = []
    for x in res:
        filename = os.path.basename(x)
        mylist.append(filename)
    return mylist