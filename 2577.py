num = 1
for _ in range(3):
    n = int(input())
    num *= n

array = [0]*10
for s in str(num):
    array[int(s)] += 1

for i in array:
    print(i)