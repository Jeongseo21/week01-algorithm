# 숫자의 개수 - 5m 55s
'''
num = 1
for _ in range(3):
    n = int(input())
    num *= n

array = [0]*10
for s in str(num):
    array[int(s)] += 1

for i in array:
    print(i)
'''





num = 1
for _ in range(3):
    num = num * int(input())

answer = [0]*10
for s in str(num):
     answer[int(s)] += 1

for n in answer:
    print(n)


















