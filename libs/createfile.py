import time
import os
import zipfile

def createFile():
    now = str(time.time())
    f = open("docs/demofile" + now + ".csv", "w")
    f.write("Woops! I have deleted the content!")
    f.close()

def createZipFile(mylist):
    now = str(time.time())
    os.chdir('build/')
    zf = zipfile.ZipFile("zipFile" + now + ".zip", mode='w')
    try:
        os.chdir('../docs/')
        for x in mylist:
            zf.write(x)
    finally:
        print('closing...')
        zf.close()
    return zf