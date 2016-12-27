# -*- coding: UTF-8 -*-
#这个用来打开图片
import numpy
import scipy
import PCA
from scipy.misc import imread
im=imread('Caltech101/1/obj1__0.png')#读入一个图片
im=imread('Caltech101/2/obj2__0.png')#读入一个图片
a=numpy.array(im,dtype=int)
print a[64]
a,b=PCA.PCA(a,1)
a=numpy.array(a,dtype=float)
b=numpy.array(b,dtype=int)
#print a
print b[64]
print numpy.shape(b)
print numpy.shape(a)