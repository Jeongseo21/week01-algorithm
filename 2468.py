from sys import *
setrecursionlimit(10 ** 6)

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# 최대값 구하기
max_num = 0
for h_list in graph:
    max_num = max(max_num, max(h_list))
# print(max_num)



def dfs(x, y):
    if x < 0 or x >= N or y <0 or y >= N:
        return False
    if tf_graph[x][y] == True:
        tf_graph[x][y] = False
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


answer = 0
# 엄청난 사실 : [[0]*N]*N 으로 선언하면 모든 리스트가 연결되서 같이 변형된다. deepcopy()해주거나 따로 생성해줘야한다.
tf_graph = [[0]*N for i in range(N)]
# T/F 그래프 만들기
for n in range(0, max_num+1): # 비가 안왔거나 max_num 이상 왔을 경우도 생각해줘야한다.
    result = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > n:
                tf_graph[i][j] = True
            else:
                tf_graph[i][j] = False
    # print(tf_graph)
    for i in range(N):
    # dfs 검사하기
        for j in range(N):
            if dfs(i, j) == True:
                result += 1
    answer = max(answer,result)

print(answer)