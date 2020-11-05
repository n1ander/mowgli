from libs import createFile, createZipFile, sortFileByTime, getFileName, sftpConnect

#createFile()
res = sortFileByTime()
mylist = getFileName(res)
zipfile = createZipFile(mylist)
#sftpConnect(zipfile)
