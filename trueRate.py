# -*- coding: UTF-8 -*-‘
#用来计算准确率的
def computeRate(labelList,labelNumber,nameList):
    resultList=[]
    numberList=[0]*labelNumber
    nameNumber=[]
    saveList=[]
    for i in xrange(labelNumber):
        for j in xrange(len(labelList)):
            if labelList==i:
                numberList[i] = numberList[i] + 1
                saveList.append(nameList[j])
        numberList[i] = numberList[i] + 1
        for k in xrange(numberList[i]):
        saveList=[]
    #统计各个标签的个数并且把同一标签下的名字放在一起

