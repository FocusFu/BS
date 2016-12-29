# -*- coding: UTF-8 -*-
#这是主成分分析算法的一个模块
from sklearn.decomposition import PCA
def myPCA(data,percent):
    pca = PCA(n_components = percent)
    lowDData = pca.fit_transform(data)
    reDData = pca.inverse_transform(lowDData)
    return lowDData , reDData
