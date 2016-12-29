# -*- coding: UTF-8 -*-
#这是主要的程序文件
import PCA
import openpicture
import clustering
import KPCA
import LaE
#import LDA
import LLE
import changename
from scipy.misc import imread

d=imread('test/obj1__0.png')
#b=PCA.PCA(d,0.99)
#print b.shape
from sklearn import *
a,b=PCA.myPCA(d,0.99)
print a.shape
print b.shape