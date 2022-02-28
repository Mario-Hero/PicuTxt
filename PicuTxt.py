#!/usr/bin/python3
# _*_ coding: UTF-8 _*_

# Created by Mario Chen, 18.02.2022, Shenzhen
# My Github site: https://github.com/Mario-Hero

import os
import sys
from chardet.universaldetector import UniversalDetector

JPG_FILE = ['.jpg', '.png', '.gif', '.jpeg', '.bmp', '.webp']
START_FLAG = b'NyOTeNGu'


def getEncodeInfo(file):
    with open(file, 'rb') as f:
        detector = UniversalDetector()
        for line in f.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        return detector.result['encoding']


def readFile(file):
    with open(file, 'rb') as f:
        return f.read()


def writeJPG(jpgPath, fileContent):
    jpgParent, jpgName = os.path.split(jpgPath)
    dotPos = jpgName.rfind('.')
    i = 1
    newJpgName = jpgName[:dotPos] + '_TXT_' + str(i) + jpgName[dotPos:]
    while os.path.exists(os.path.join(jpgParent, newJpgName)):
        i += 1
        newJpgName = jpgName[:dotPos] + '_TXT_' + str(i) + jpgName[dotPos:]
    with open(jpgPath, 'rb') as readJPG:
        newFileContent = readJPG.read() + START_FLAG + fileContent
    with open(os.path.join(jpgParent, newJpgName), 'wb') as writeNew:
        writeNew.write(newFileContent)


if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1].endswith('.txt'):
            txtPath = sys.argv[1]
            jpgPath = sys.argv[2]
        else:
            txtPath = sys.argv[2]
            jpgPath = sys.argv[1]
        fileContent = readFile(txtPath)
        encodeInfo = getEncodeInfo(txtPath)
        if encodeInfo != 'utf-8':
            fileDecode = fileContent.decode(encodeInfo, 'ignore')
            fileContent = fileDecode.encode('utf-8')
        #encodeInfo = getEncodeInfo(txtPath)
        #print(encodeInfo)
        writeJPG(jpgPath, fileContent)
    elif len(sys.argv) == 2:
        nameLower = sys.argv[1].lower()
        for ext in JPG_FILE:
            if nameLower.endswith(ext):
                findTxt = False
                with open(sys.argv[1], 'rb') as f:
                    data = f.read()
                    result = data.rfind(START_FLAG)
                    #print(result)
                    if result != -1:
                        try:
                            print(data[(result + len(START_FLAG)):].decode(encoding='utf-8'))
                            findTxt = True
                            os.system('pause')
                        except:
                            pass
                    else:
                        print('There aren\'t any words in this picture.')
                if not findTxt:
                    txt = input('Please enter the text you want to embed into the picture:\n')
                    if txt:
                        fileContent = txt.encode('utf-8')
                        writeJPG(sys.argv[1], fileContent)
                        print('Finish.')
                        os.system('pause')
            break

