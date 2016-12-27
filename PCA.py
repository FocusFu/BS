# -*- coding: UTF-8 -*-
#这是主成分分析算法的一个模块
'''这是一个降维函数，输入：
data——要降维的原始数据
aim——一个百分比，小于1
返回降维后的数据'''
import numpy
import scipy
def zeroMean(dataMat):#零均值化函数
    meanVal=numpy.mean(dataMat,axis=0)#按列求均值
    newData=dataMat-meanVal#按列零均值化
    return newData,meanVal
def percentage2n(eigVals,percentage):
    sortArray=numpy.sort(eigVals)#升序
    sortArray=sortArray[-1::-1]#逆转，即降序
    arraySum=sum(sortArray)
    tmpSum=0
    num=0
    for i in sortArray:
        tmpSum+=i
        num+=1
        if tmpSum>=arraySum * percentage:
            return num
def PCA(data,aim):#PCA函数
    dataMat=data
    newData,meanVal=zeroMean(dataMat)#零均值化
    covMat=numpy.cov(newData,rowvar=0)#协方差矩阵
    eigVals,eigVects=numpy.linalg.eig(numpy.mat(covMat))#eigVals行向量特征值，eigVects特征向量
    n=percentage2n(eigVals,aim)
    eigValIndice = numpy.argsort(eigVals) # 对特征值从小到大排序  
    n_eigValIndice= eigValIndice[-1:-(n + 1):-1]# 最大的n个特征值的下标  
    n_eigVect = eigVects[:, n_eigValIndice]# 最大的n个特征值对应的特征向量  
    lowDDataMat = newData * n_eigVect# 低维特征空间的数据  
    reconMat = (lowDDataMat * n_eigVect.T) + meanVal# 重构数据  
    return lowDDataMat, reconMat