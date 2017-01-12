# -*- coding: UTF-8 -*-
#这是主成分分析算法的一个模块，加一个归一化
from sklearn.decomposition import PCA
import numpy as np
def myPCA(data,percent):
    pca = PCA(n_components = percent,copy=True,whiten=False,svd_solver='auto')
    lowDData = np.array( pca.fit_transform(data))
    reDData = pca.inverse_transform(lowDData)
    maxData=np.max(lowDData,axis=0)
    minData=np.min(lowDData,axis=0)
    rangeData=maxData-minData
    lowDData=lowDData/rangeData
    return lowDData , reDData