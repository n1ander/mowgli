from libs import createFile, createZipFile, sortFileByTime, getFileName

createFile()
res = sortFileByTime()
mylist = getFileName(res)
createZipFile(mylist)