import math

a, b, v = map(int, input().split())
day = a-b

print(math.ceil((v - a)/day) + 1)


'''
math.ceil(i) : 올림

math.floor(i) : 내림

math.trunc(i) : 버림
'''
