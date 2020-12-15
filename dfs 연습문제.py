# 세로길이 : n, 가로길이 : m

n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 특정노드를 방문한 뒤 재귀로 연결된 모든 노드 방문/ 세로가 x(행), 가로가 y(열)
def dfs(x, y):
    # 범위를 벗어나면 종료
    if x<0 or x>=n or y<0 or y>= m:
        return False
    # 현재 노드를 방문하지 않았거나 막혀있지 않은 경우
    if graph[x][y] == 0:
        # 방문처리
        graph[x][y] = 1
        # 상하좌우 호출해서 재귀로 dfs확인
        dfs(x-1, y) #상
        dfs(x+1, y) #하
        dfs(x, y-1) #좌
        dfs(x, y+1) #우
        return True # 네 방향 다 True면
    # 중간에 False로 튕겨저 나오면
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)