import time
import os
import zipfile

def createFile():
    now = time.strftime('%Y%m%d', time.gmtime())
    f = open("docs/demofile" + now + ".csv", "w")
    f.write("Woops! I have deleted the content!")
    f.close()

def createZipFile(mylist):
    now = time.strftime('%Y%m%d', time.gmtime())
    os.chdir('build/')
    zf = zipfile.ZipFile("CustomerX" + now + ".zip", mode='w')
    try:
        os.chdir('../../CEWIS/out/')
        for x in mylist:
            zf.write(x)
    finally:
        os.chdir('../../mowgli/docs/')
        print('closing...')
        zf.close()
    return zf