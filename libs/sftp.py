import pysftp
import time
import smtplib

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

host = ""
port = 25
sender = ""
receiver = ""
message = "From: " + sender + "\r\nTo: " + "<Automated Email>" + "\r\nSubject: Email Notification " + "\r\n\r\nFile has been sent successfully!" 

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

def sendEmail():
    try:
        obj = smtplib.SMTP(host, port)
        obj.sendmail(sender, receiver, message)
    except smtplib.SMTPException:
        print("Error, email did not send.")



