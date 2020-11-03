import pysftp
import time

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

def sftpConnect(file):
    now = str(time.time())
    file = "../build/" + file.filename
    remfile = "sites" + now + ".zip"
    try:
        with pysftp.Connection('localhost', username='tester', password='password', cnopts=cnopts) as sftp:
            sftp.put(file, remfile)
            print("Successfully connected to SFTP...")
    except:
        print("SFTP connection failed!")


