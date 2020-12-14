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
'''
# 도수정렬 - 메모리 초과

# 수 입력받기

N = int(input())
a = [0]*N # 4*100000000 = 400000000
for i in range(N):
    a[i] = int(input())

# 도수 분표포 만들기
f = [0] * 10001 # 4*10001 = 40004
for score in a:
    f[score] += 1


# 누적 도수분표포 만들기
sum_score = 0
for i in range(len(f)):
    sum_score += f[i]
    f[i] = sum_score


# 새로운 배열에 정렬하기
b = [0]*N # 4*100000000 = 400000000
for i in range(N-1, -1, -1):
    f[a[i]] -= 1
    b[(f[(a[i])])] = a[i]

# 출력
for _ in b:
    print(_)
'''

# 도수정렬 - 시간초과

# 수 입력받기
import sys

N = int(input())
# 도수 분표포 만들기
f = [0] * 10001 # 4*10001 = 40004
for _ in range(N):
    f[int(input())] += 1


# 누적 도수분표포 만들기
sum_score = 0
for i in range(len(f)):
    sum_score += f[i]
    f[i] = sum_score


#누적분포표까지 완성
for i in range(len(f)):
    if i == 0:
        for _ in range(f[0]):
            print(i)
        # print(f'{i}' * f[0], end='')
    else:
        for _ in range(f[i] - f[i-1]):
            print(i)

        # print(f'{i}' * (f[i]-f[i-1]), end='')
