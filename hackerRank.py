from collections import deque
dec = deque()
sw = {
    "append": dec.append,
    "appendleft": dec.appendleft,
    "pop": dec.pop,
    "popleft": dec.popleft
}
n = int(input())
for i in range(n):
    data = list(map(str,input().split()))
    try:
        sw[data[0]](int(data[1]))
    except:
        sw[data[0]]()