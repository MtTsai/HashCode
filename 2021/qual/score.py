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
# main prog 
####################
for fileName in inFiles:
    ofName = "_" + fileName + ".out"

    print("Start: " + fileName)

    with open(fileName,"r") as f:
        D, I, S, V, F = map(int, f.readline().split())

        allSt = {}
        iStEndList = [[] for _ in range(I)]
        stQueue = {}
        for _ in range(S):
            B, E, st, L = f.readline().split()
            B, E, L = map(int, [B, E, L])
            iStEndList[E].append(st)
            allSt[st] = [B, E, L]
            stQueue[st] = []

        carPath = []
        for cid in range(V):
            p = f.readline().split()[1:]
            carPath.append(p)
            st = p[0]
            stQueue[st].append((cid, 0, 0)) # cid, stIdx, passSec

    with open(ofName, "r") as f:
        A = int(f.readline())
        iStPassList = [[] for _ in range(I)]
        for _ in range(A):
            iid = int(f.readline())
            stCnt = int(f.readline())
            for __ in range(stCnt):
                stName, sec = f.readline().split()
                sec = int(sec)
                iStPassList[iid] += [stName] * sec

        score = 0
        for t in range(D):
            for iid in range(I):
                if len(iStPassList[iid]) == 0:
                    continue
                passStIdx = t % len(iStPassList[iid])
                passSt = iStPassList[iid][passStIdx]

                if len(stQueue[passSt]) == 0:
                    continue

                cid, stIdx, passSec = stQueue[passSt][0]
                if passSec > t:
                    continue

                stQueue[passSt].pop(0)
                stIdx += 1
                nextSt = carPath[cid][stIdx]
                nextStLen = allSt[nextSt][2]
                nextEndTime = t + nextStLen
                if stIdx == len(carPath[cid]) - 1:
                    if nextEndTime <= D:
                        score = score + F + D - nextEndTime
                else:
                    stQueue[nextSt].append((cid, stIdx, nextEndTime))
        print(ofName + ": " + str(score))
