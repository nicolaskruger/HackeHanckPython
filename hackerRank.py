from itertools import product
def calc(li,m=0):
    sum = 0
    for l in li:
        sum+=l*l
    return sum%m
def makeMap(prod,m):
    mp ={}
    for p in prod:
        try:
            mp[calc(p,m)].append(p)
        except:
            mp[calc(p,m)]=[p]
    return mp
(n,m) = map(int,input().split())
#print(n,m)
li =[]
for i in range(n):
    l = set(map(int,input().split()))
    li.append(l)
#print(li)
prod = set(product(*li))
mp=(makeMap(prod,m))
keys = list(mp.keys())
keys.sort()
# for k in keys:
#     print(k,mp[k])
print(keys[len(keys)-1])