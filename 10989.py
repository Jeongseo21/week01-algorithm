'''
# 계수정렬 - 메모리 초과

array = [0]*10000
nums = []
N = int(input())
for i in range(N):
    nums.append(int(input()))

while not nums == []:
    array[nums.pop()] += 1

for i in range(len(array)):
    for j in range(array[i]):
        print(i)
'''

# 도수정렬
