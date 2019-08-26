import os
from shutil import copyfile


def getListOfFiles(dir_name):
    listOfFile = os.listdir(dir_name)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dir_name[53:], entry[:])
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    pdfFiles = []
    for file in allFiles:
        if file.endswith('.pdf'):
            pdfFiles.append(file)
    return pdfFiles

dir_mid ='Put/Your/path/here'
dir_name = ['/finalsubdirectory'];
numberlist = []
for i in dir_name:
    j = dir_mid + i
    k = getListOfFiles(j)
    for l in k:
        m = l.split('_')
        numberlist.append(m[1:2])
print (numberlist)
 