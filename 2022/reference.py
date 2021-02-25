import collections
import os
import sys
import random 

inFiles = ["a"]
        "b",
        "c",
        "d",
        "e"]

####################
# utility
####################
def parsing(inputfile):
    with open(inputfile,"r") as f:
        N = map(int, f.readline().split())
        for line in f.readlines():
            p = line.split()
    return N,p
    
def score():
    return 0

def output(fileName):
    with open(fileName,"w") as f:
        f.write("balabalabala\n") 

####################
# main prog 
####################
for f in inFiles:
    data = parsing(f)
output("test")
    




