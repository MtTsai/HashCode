#!/usr/bin/env python

from functools import reduce
from copy import deepcopy

# fileIn = "a_example"
# fileIn = "b_little_bit_of_everything.in"
fileIn = "c_many_ingredients.in"
# fileIn = "d_many_pizzas.in"
# fileIn = "e_many_teams.in"

f = open(fileIn, "r")

import sys
sys.setrecursionlimit(10**6)

M, T2, T3, T4 = [int(x) for x in f.readline().strip().split()]

pizzas = {}
vis = {}
pidCntList = []
for pid in range(M):
    pline = f.readline().strip().split()
    ing = set(pline[1:])
    pizzas[pid] = ing
    vis[pid] = False
    pidCntList.append([-len(ing), pid])

sortIdList = [j for i, j in sorted(pidCntList)]

def ingCnt(pidList):
    return len(reduce(lambda x, y: x.union(y), [pizzas[pid] for pid in pidList], set()))

# def markV(pidList, v):
#     for pid in pidList:
#         vis[pid] = v

# def getOpt(d, curList = [], optList = []):
#     if d:
#         for pid in sortIdList:
#             if not vis[pid] and pid not in curList:
#                 optList = getOpt(d - 1, curList + [pid], optList)
#                 return optList
#         return optList
#     else:
#         curCnt = ingCnt(curList)
#         optCnt = ingCnt(optList)
#         return curList if curCnt > optCnt else optList
pIdx = 0

def markV(tl, v):
    global pIdx
    pIdx += len(tl) if v else -len(tl)

def getOpt(d):
    optList = []
    global pIdx
    if pIdx + d <= len(sortIdList):
        optList = sortIdList[pIdx:pIdx+d]
    return optList

gOut = []
gScore = 0
dp = set()
def distPizza(tList, outline, score, m):
    global dp
    tHash = reduce(lambda x, y: x * 1e5 + y, tList)
    if tHash in dp:
        return
    dp.add(tHash)
    # print(tList)
    for i in [2, 1, 0]:
        if tList[i]:
            tv = i + 2
            if m < tv:
                return

            tl = getOpt(tv)
            if tl:
                tList[i] -= 1
                outline.append([tv] + tl)
                addScore = pow(ingCnt(tl), 2)
                score += addScore
                markV(tl, True)

                global gOut, gScore
                if score > gScore:
                    gOut = outline.copy()
                    gScore = score

                distPizza(tList, outline, score, m - tv)

                if m < 50:
                    outline.pop()
                    score -= addScore
                    markV(tl, False)
                    tList[i] += 1

# print(getOpt(2))
# print(getOpt(3))
# print(getOpt(4))

distPizza([T2, T3, T4], [], 0, M)
with open(fileIn[0] + ".txt", "w") as of:
    of.write(str(len(gOut)) + "\n")
    of.write("\n".join([" ".join([str(v) for v in l]) for l in gOut]))
print(gScore)

# print(sum([x[0] for x in gOut]))
