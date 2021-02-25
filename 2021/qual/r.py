#!/usr/bin/env python3

import collections
import os
import sys
import random 

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
    with open(fileName,"r") as f:
        D, I, S, V, F = map(int, f.readline().split())

        B = []
        E = []
        stName = []
        L = []
        iStEndList = [[] for _ in range(I)]
        for _ in range(S):
            BIn, EIn, stNameIn, LIn = f.readline().split()
            B.append(int(BIn))
            E.append(int(EIn))
            stName.append(stNameIn)
            L.append(int(LIn))
            iStEndList[int(EIn)].append(stNameIn)

        carPath = []
        for _ in range(V):
            carPath.append(f.readline().split()[1:])

    with open(fileName + ".out", "w") as f:
        f.write(str(I) + "\n")
        for iid in range(I):
            if len(iStEndList[iid]) > 0:
                f.write(str(iid) + "\n")
                f.write(str(len(iStEndList[iid])) + "\n")
                for stName in iStEndList[iid]:
                    f.write(stName + " " + str(1) + "\n")

    




