#!/usr/bin/env python

from functools import reduce
from copy import deepcopy


# fileIn = "dataSet/a_example.txt"
# fileIn = "dataSet/b_read_on.txt"
# fileIn = "dataSet/c_incunabula.txt"
# fileIn = "dataSet/d_tough_choices.txt"
# fileIn = "dataSet/e_so_many_books.txt"
# fileIn = "dataSet/f_libraries_of_the_world.txt"

import sys
sys.setrecursionlimit(10**6)

totalSc = 0
for fileIn in [
    "dataSet/a_example.txt",
    "dataSet/b_read_on.txt",
    "dataSet/c_incunabula.txt",
    "dataSet/d_tough_choices.txt",
    "dataSet/e_so_many_books.txt",
    "dataSet/f_libraries_of_the_world.txt"]:

    with open(fileIn, "r") as f:
    
        B, L, D = map(int, f.readline().strip().split())
        
        bookSc = [int(x) for x in f.readline().strip().split()]
        
        N = [0 for _ in range(L)]
        T = [0 for _ in range(L)]
        M = [0 for _ in range(L)]
        libBList = [[] for _ in range(L)]
        for lib in range(L):
            # T is signup time, M is shipping number per day
            N[lib], T[lib], M[lib] = map(int, f.readline().strip().split())
            libBList[lib] = map(int, f.readline().strip().split())

            tmpB = [[-bookSc[bid], bid] for bid in libBList[lib]]
            libBList[lib] = [bid for _, bid in sorted(tmpB)]
        
        sortLibList = sorted([[T[lib], -M[lib], -N[lib], lib] for lib in range(L)])
        sortLibList = [lib for t, _, _, lib in sortLibList]
        
        # Skip output, directly scoring it
        # with open(fileIn[0] + ".txt", "w") as of:
        #     of.write(str(L) + "\n")
        #     for lib in range(L):
        #         of.write(" ".join([str(v) for v in [lib, N[lib]]]) + "\n")
        #         of.write(" ".join([str(v) for v in libBList[lib]]) + "\n")
        
        bVis = set()
        def scoreL(startD, lib, bList):
            sc = 0
            global T, D, bVis
            remainD = D - (startD + T[lib])
            if remainD > 0:
                maxShipN = remainD * M[lib]
                for bid in bList[:maxShipN]:
                    if bid not in bVis:
                        sc += bookSc[bid]
                        bVis.add(bid)
            return sc
        
        def score(ofList):
            sc, currD = 0, 0
            for lib, bList in ofList:
                sc += scoreL(currD, lib, bList)
                global T
                currD += T[lib]
            return sc
        

        bbVis = set()
        ofList = []
        for lib, bList in [[lib, libBList[lib]] for lib in sortLibList]:
            tmpBList = []
            for bid in bList:
                if bid not in bbVis:
                    bbVis.add(bid)
                    tmpBList.append(bid)
            ofList.append([lib, tmpBList])

        t = score(ofList)
        # t = score([[lib, libBList[lib]] for lib in range(L)])
        totalSc += t
        print(t, totalSc)
    
print(totalSc)
