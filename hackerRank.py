from collections import OrderedDict

def makeMap(s):
    dic = OrderedDict()
    for c in s:
        try:
            dic[c]+=1
        except:
            dic[c]=1
    return dic
def invDic(dic):
    inv =OrderedDict()
    for key,val in dic.items():
        try:
            inv[val].append(key)
            inv[val].sort()
        except:
            inv[val]=[]
            inv[val].append(key)
    return inv
def showBest(dic):
    key = list(dic.keys())
    key.sort()
    n =3
    for i in reversed(range(len(dic))):
        for v in dic[key[i]]:
            print(" ".join([v,str(key[i])]))
            n-=1
            if n<=0:
                return
        
if __name__ == '__main__':
    s = input()
    dic = makeMap(s)
    inv = invDic(dic)
    showBest(inv)