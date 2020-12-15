# 문자열 반복 - 8m 48s

'''
n = int(input())
data = []
for _ in range(n):
    data.append(input().split())

for i in range(n):
    num = int(data[i][0])
    str = data[i][1]
    for s in str:
        print(s*num, end='')
    print()
'''



N = int(input())
array = []
for _ in range(N):
    array.append(tuple(input().split()))

print(array)

for c in array:
    for i in range(len(c[1])):
        print(c[1][i] * int(c[0]), end="")

















