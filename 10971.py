import itertools

N = int(input())
costs=[]
for _ in range(N):
    costs.append(list(map(int, input().split())))

# 모든 경우의 수 구하기
arr = [1, 2, 3, 4]
nPr = itertools.permutations(arr, 4)
arrays = list((nPr))
new = []
for i in range(len(arrays)):
    new.append(list(arrays[i]))
    new[i].append(new[i][0])
print(new)
# 비용 구하기
answer = []

for n in new:
    cost = 0
    for j in range(0, len(n)-1):
        if j+1 == 4:
            cost += costs[4][0]
        cost += costs[j][j+1]
    answer.append(cost)
print(answer)


