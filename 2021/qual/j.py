#!/usr/bin/env python3

import math
import collections
import os
import sys
import random 
from functools import reduce
from copy import deepcopy

inFiles = ["a.txt",
        "b.txt",
        "c.txt",
        "d.txt",
        "e.txt",
        "f.txt"]
a = ["a.txt"]

####################
# utility
####################
def score():
    return 0

def output(fileName):
    with open(fileName,"w") as f:
        f.write("balabalabala\n") 

####################
# main prog 
####################
for fileName in inFiles:
    print("Start: " + fileName)
    with open(fileName,"r") as f:
        D, I, S, V, F = map(int, f.readline().split())

        allSt = {}
        iStEndList = [[] for _ in range(I)]
        for _ in range(S):
            B, E, st, L = f.readline().split()
            B, E, L = map(int, [B, E, L])
            iStEndList[E].append(st)
            allSt[st] = [B, E, L]

        carPath = []
        #allPathCount = collections.Counter()
        allPathWeight = collections.defaultdict(float)
        beginSt = set()
        for _ in range(V):
            p = f.readline().split()[1:]
            
            #pathTime = sum([allSt[s][2] for s in p])
            # filter unreachable car path
            #if pathTime <= D*0.8:
            carPath.append(p)
            beginSt.add(p[0])
            for s in p:
                allPathWeight[s] += 100000/len(p)
            #print(allPathWeight)

        #allPathCount = reduce(lambda x, y: x + collections.Counter(y), carPath, collections.Counter())

    ofData = []
    for iid in range(I):
        if len(iStEndList[iid]) > 0:
            stTimeList = []
            base = 0
            for st in iStEndList[iid]:
                if allPathWeight[st] > 0:
                    tmpTime = float(allPathWeight[st] / float(allSt[st][2]))
                    stTimeList.append([st, tmpTime])
            
            if len(stTimeList):
                s = sum(tmpTime for st, tmpTime in stTimeList)
                m = min(allSt[st][2] for st, tmpTime in stTimeList)/len(stTimeList)

                for i in range(len(stTimeList)):
                    stTimeList[i][1]= int(max(1,((stTimeList[i][1]/s)*m)))

                ofData.append([iid, stTimeList])

    with open(fileName + ".out", "w") as f:
        f.write(str(len(ofData)) + "\n")
        for iid, stTimeList in ofData:
            if stTimeList =="0":
                continue
            f.write(str(iid) + "\n")
            f.write(str(len(stTimeList)) + "\n")
            for st, stTime in stTimeList:
                f.write(st + " " + str(stTime) + "\n")
