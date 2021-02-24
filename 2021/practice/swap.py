import collections
import random 
import os

in_a = "a_example"
in_b = "b_little_bit_of_everything"
in_c = "c_many_ingredients"
in_d = "d_many_pizzas"
in_e = "e_many_teams"
inputdir = in_c
inputfile = in_c+".in"

def getScore(pizzas):
    alling = []
    for p in pizzas:
        for g in pizza[p]:
            alling.append(g)
    return len(collections.Counter(alling))**2

####################
# deal with input
####################

f = open(inputfile)
pNum, T1, T2, T3 = map(int, f.readline().split())
pizza = []
ingre = collections.defaultdict(int) 

for line in f.readlines():
    p = line.split()[1:]
    pizza.append(p)
    for ing in p:
        ingre[ing]+=1
f.close()        

####################
# random chosed and and read ans 
####################
files = os.listdir("./"+inputdir)
files.remove('.DS_Store')
ans= list(map(lambda x: int(os.path.splitext(x)[0]),files ))
ans.sort()
idx = -random.randint(1,100)%len(ans)
oriScore = ans[idx]
print(f"try{oriScore}")
f = open(inputdir + "/"+str(ans[idx])+".txt")
teams = f.readline() 
ret = []
for line in f.readlines():
    ret.append(list(map(int,line.split()))[1:])
#print(ret)

####################
# random swap 
####################
for _ in range(max(pNum//100,5)):
    a = random.randint(0,len(ret)-1)
    b = random.randint(0,len(ret)-1)
    a_p = random.randint(0,len(ret[a])-1)
    b_p = random.randint(0,len(ret[b])-1)
    oldS = getScore(ret[a])+getScore(ret[b])
    ret[a][a_p], ret[b][b_p] = ret[b][b_p], ret[a][a_p] 
    newS = getScore(ret[a])+getScore(ret[b])
    if newS > oldS: 
        continue
    ret[a][a_p], ret[b][b_p] = ret[b][b_p], ret[a][a_p] 
    #print(a,b,a_p,b_p)

####################
# calcute score and output files
####################

score = 0
for r in ret:
    score += getScore(r)
if score > oriScore:
    f = open("./"+inputdir+"/"+str(score)+".txt","w")
    f.write(str(len(ret))+"\n")
    for r in ret:
        if not r:
            continue
        f.write(str(len(r))+" "+" ".join(map(str,r))+"\n")
    print("find new ans!! ", score, ">", oriScore)


#print(pNum, T1, T2, T3)
#print(ret)
#print(pizza)
#print(ingre)



