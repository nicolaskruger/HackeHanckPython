from collections import deque
dec = deque()
def isValid(dec):
    cur = float('inf')
    for i in range(len(dec)):
        n = len(dec)-1
        ncur=0
        if dec[0]> dec[n]:
            ncur= dec[0]
            dec.popleft()
        else:
            ncur= dec[n]
            dec.pop()
        if ncur> cur:
            return False
        cur = ncur
    return True
for i in range(int(input())):
    input()
    dec = deque(map(int,input().split()))
    print(isValid(dec))
