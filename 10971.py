'''
# 완전탐색으로 구현 - 시간초과

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

'''
'''
# dfs로 구현 - python3 시간초과, pypy3 통과
N = int(input())

way = [0]*N
visited = [0]*N

for i in range(N):
    way[i] = list(map(int, input().split()))

ans = 1e9

# dfs함수 구현
def dfs(origin, pos, cnt, cost):
    # 마지막 지점에서 시작 지점으로 가는 카운트라면
    if cnt == N-1:
        # 마지막 지점에서 시작 지점으로 가는 길이 없으면 리턴
        if way[pos][origin] == 0:
            return
        else:
            # 마지막 지점에서 시작 지점으로 가는 비용을 총 비용에 더해주고
            cost += way[pos][origin]
            global ans
            # 기존에 저장해놓은 ans랑 현재 비용을 비교해서 최소값을 ans에 저장
            ans = min(ans, cost)
            return

    # 아직 마지막 지점이 아닐 때
    for i in range(N):
        # i 도시에 간적없고 현재 도시에서 i 도시로 가는 길이 있을 때
        if visited[i] == 0 and way[pos][i] > 0:
            # i 도시에 방문처리 해주고
            visited[i] = 1
            # 시작점 origin을 계속 저장해주고 현재 지점을 i로 이동, cnt 1 증가, 비용은 기존 cost에 현재위치에서 i로 가는 비용 추가
            dfs(origin, i, cnt+1, cost+way[pos][i])
            visited[i] = 0


for i in range(N):
    for j in range(N):
        if way[i][j] > 0 :
            visited[i] = 1
            visited[j] = 1
            dfs(i, j, 1, way[i][j])
            visited[i] = 0
            visited[j] = 0

print(ans)
'''

N = int(input())
way = []
visited = [0]*N
ans = 1e9

for i in range(N):
    way.append(list(map(int, input().split())))

def dfs(origin, pos, cnt, cost):
    global ans
    if cnt == N-1:
        if way[pos][origin] == 0:
            return
        else:
            ans = min(ans, cost + way[pos][origin])
            return
    for i in range(N):
        if visited[i] == 0 and way[pos][i] > 0:
            visited[i] = 1
            dfs(origin, i, cnt+1, cost+way[pos][i])
            visited[i] = 0



for i in range(N):
    for j in range(N):
        if way[i][j] > 0:
            visited[i] = 1
            visited[j] = 1
            dfs(i, j, 1, way[i][j])
            visited[i] = 0
            visited[j] = 0

print(ans)