import os
from shutil import copyfile


def getListOfFiles(dir_name):
    listOfFile = os.listdir(dir_name)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dir_name[53:], entry[5:12])
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    pdfFiles = []
    for file in allFiles:
        if file.endswith('0') or file.endswith('1') or file.endswith('2') or file.endswith('3') or file.endswith('4') or file.endswith('5') or file.endswith('6') or file.endswith('7') or file.endswith('8') or file.endswith('9'):
            pdfFiles.append(file)
    return pdfFiles

dir_mid ='Put/Your/path/here'
dir_name = ['/finalsubdirectory'];
for i in dir_name:
    j = dir_mid + i
    k = getListOfFiles(j)
    print(f"\n pdf files in the {i[1:55]} folder ")
    print (*k, sep = '\n')