import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
with pysftp.Connection('localhost', username='tester', password='password', cnopts=cnopts) as sftp:
    print("Successfully connected to SFTP...")