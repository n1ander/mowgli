from libs import createFile, createZipFile, sortFileByTime, getFileName, sftpConnect

res = sortFileByTime()
mylist = getFileName(res)
zipfile = createZipFile(mylist)
sftpConnect(zipfile)