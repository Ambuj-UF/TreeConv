# This program executes ID3 machine learning algorithm to obtain the depth of descesion tree from matrix data produced
# by running MatrixCol.py program.
# The standard ID3 source code was taken from the blog page (http://www.jdxyw.com/?p=2095) of 
# Yongwei Xing, SharePoint/MOSS developer at Shanghai,China.  
# Few additional modifications were conducted to make it suitable for our program

from string import split
import math
import operator

def majorityCnt(classlist):
    classcount={}
    for vote in classlist:
        if vote not in classcount.keys():
            classcount[vote]=0
        classcount[vote] += 1
    sortedClassCount=sorted(classcount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def entropy(dataset):
    n=len(dataset)
    labels={}
    for record in dataset:
        label=record[-1]
        if label not in labels.keys():
            labels[label]=0
        labels[label]+=1
    ent=0.0
    for key in labels.keys():
        prob=float(labels[key])/n
        ent= -prob*math.log(prob,2)
    return ent

def splitDataset(dataset,nclom,value):
    retDataSet=[]
    for record in dataset:
        if record[nclom] == value:
            reducedRecord=record[:nclom]
            reducedRecord.extend(record[nclom+1:])
            retDataSet.append(reducedRecord)
    return retDataSet

def chooseBestFeatureToSplit(dataset):
    numberFeature=len(dataset[0])-1
    baseEntropy=entropy(dataset)
    bestInfoGain=0.0
    bestFeature=-1
    for i in range(numberFeature):
        featureList=[x[i] for x in dataset]
        uniqueValues=set(featureList)
        newEntropy=0.0
        for value in uniqueValues:
            subDataset=splitDataset(dataset, i, value)
            prob=len(subDataset)/float(len(dataset))
            newEntropy += prob*entropy(subDataset)
        infoGain=baseEntropy-newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain=infoGain
            bestFeature=i
    return bestFeature

def buildTree(dataset,labels):
    classlist=[ x[-1] for x in dataset]
    if classlist.count(classlist[0]) == len(classlist):
        return classlist[0]
    if len(classlist)==1:
        return majorityCnt(classlist)
    bestFeature=chooseBestFeatureToSplit(dataset)
    bestFeatureLabel=labels[bestFeature]
    tree={bestFeatureLabel:{}}
    del(labels[bestFeature])
    featValues = [x[bestFeature] for x in dataset]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        tree[bestFeatureLabel][value] = buildTree(splitDataset(dataset, bestFeature, value),subLabels)
    return tree

def walk_dict(d,depth=0):
    for k,v in sorted(d.items(),key=lambda x: x[0]):
        if isinstance(v, dict):
            print ("  ")*depth + ("%s" % k)
            walk_dict(v,depth+1)
        else:
            print ("  ")*depth + "%s %s" % (k, v)


fs=open("outMat.txt")
dataset=[]
for line in fs:
    lineSplit=split(line[:-1],"\t")
    lineSplit = lineSplit[:-1]
    dataset.append([float(value) for value in lineSplit])
fs.close()
nfeature=len(dataset[0])
labels=["att"+str(i) for i in range(nfeature-1)]

labels2=[x for x in labels]

tree=buildTree(dataset, labels)

walk_dict(tree)



