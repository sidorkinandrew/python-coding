# https://stepik.org/lesson/294080/step/6?unit=275759
# put your python code here
import numpy
n = list(map(int,list(input())))
print(n.count(3))
print(n.count(n[-1]))
print(len([1 for i in n if i%2==0]))
print(sum([i for i in n if i>5]))
print(numpy.prod([1]+[i for i in n if i in [8,9]]))
print(sum([1 for i in n if i==5 or i==0]))
