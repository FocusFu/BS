# -*- coding: UTF-8 -*-
#不知道为什么，图片的顺序是乱的，这个文件主要整理一下顺序
def arrangeData(imageData,addressList):
    length=len(imageData)
    rangeImage=[1]*length
    rangeList=['a']*length
    for i in xrange(length):
        j=int(addressList[i][3])-1
        if addressList[i][7]=='.':
            j=j*72+int(addressList[i][6])
        else:
            j = j * 72 + int(addressList[i][6])*10+int(addressList[i][7])
        rangeImage[j]=imageData[i]
        rangeList[j]=addressList[i]
    return rangeImage,rangeList
