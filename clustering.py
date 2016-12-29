# -*- coding: UTF-8 -*-‘
#聚类算法暂时使用k-means
from sklearn.cluster import KMeans
def myKmeans(data,clusters):
    K_Means = KMeans(n_clusters=clusters,random_state=0)
    reLabel=K_Means.fit(data)
    return reLabel