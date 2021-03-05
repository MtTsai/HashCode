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
        allPathCount = collections.Counter()
        beginSt = set()
        endSt = set()

        carStCnt = 0
        carStCntHist = []
        for _ in range(V):
            p = f.readline().split()[1:]
            carPath.append(p)
            beginSt.add(p[0])
            endSt.add(p[-1])
            carStCnt += len(p)
            carStCntHist.append(len(p))

        carStCntThr = sorted(carStCntHist)[int(V * 0.8)]

        tgtPath = []
        for i in range(V):
            p = carPath[i]
            if len(p) <= carStCntThr:
                tgtPath.append(p)

        allPathCount = reduce(lambda x, y: x + collections.Counter(y), tgtPath, collections.Counter())

        iCarCnt = [0] * I
        for iid in range(I):
            for st in iStEndList[iid]:
                iCarCnt[iid] += allPathCount[st]

    ofData = []
    for iid in range(I):
        if len(iStEndList[iid]) > 0:
            stTimeList = []
            base = 0
            stCnt = len(iStEndList[iid])
            for st in iStEndList[iid]:
                if allPathCount[st] > 0:
                    tmpTime = allPathCount[st] * stCnt / iCarCnt[iid]
                    tmpTime = math.ceil(tmpTime)
                    stTimeList.append([0 if st in beginSt else 1, [st, tmpTime]])
                    if base == 0 or base > tmpTime:
                        base = tmpTime

            stTimeList = [stTime for _, stTime in sorted(stTimeList)]
            # stTimeList = [[st, min(D / 2, math.ceil(tmpTime / base))] for st, tmpTime in stTimeList]
            if len(stTimeList) > 0:
                ofData.append([iid, stTimeList])

    with open("_" + fileName + ".out", "w") as f:
        f.write(str(len(ofData)) + "\n")
        for iid, stTimeList in ofData:
            f.write(str(iid) + "\n")
            f.write(str(len(stTimeList)) + "\n")
            for st, stTime in stTimeList:
                f.write(st + " " + str(int(stTime)) + "\n")
