# -*- coding: UTF-8 -*-
#这是主要的程序文件
import PCA
import openpicture
import numpy
from sklearn.cluster import KMeans
#from scipy.misc import imread
#d=imread('test/obj1__0.png')
#b=PCA.PCA(d,0.99)
#print b.shape
from sklearn import *
#a,b=PCA.myPCA(d,0.99)
#print a.shape
#print b.shape
a = 'test/'
im,l = openpicture.openPictures(a)
#d,c = PCA.myPCA(im,0.9)
f=[]
for i in xrange(len(im)):
    z,ff = PCA.myPCA(im[i],0.9)
    f.append(numpy.transpose(z))
K_Means = KMeans(n_clusters=2).fit(z.T)
label=K_Means.labels_
print K_Means.labels_
print l
print K_Means.labels_


