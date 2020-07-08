import numpy
(n,m)= map(int,input().split())
array = []
for _ in range(n):
    array.append(list(map(int,input().split())))
array= numpy.array(array)
numpy.set_printoptions(legacy='1.13')
print(numpy.mean(array,1))
print(numpy.var(array,0))
print(numpy.std(array))