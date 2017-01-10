# -*- coding: UTF-8 -*-
#拉普拉斯特征映射算法
from sklearn.cluster import KMeans
import numpy as np
X = [[1, 2], [1, 4], [1, 0],[4, 2], [4, 4], [4, 0]]
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print kmeans.labels_