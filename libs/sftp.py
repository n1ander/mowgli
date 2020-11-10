import pysftp
import time

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

def sftpConnect(file):
    now = time.strftime('%Y%m%d%H%M%S', time.gmtime())
    file = "../build/" + file.filename
    remfile = "sites" + now + ".zip"
    try:
        with pysftp.Connection('localhost', username='tester', password='password', cnopts=cnopts) as sftp:
            sftp.put(file, remfile)
            print("Successfully connected to SFTP...")
    except:
        print("SFTP connection failed!")


