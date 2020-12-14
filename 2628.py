# 가로길이 col, 세로길이 row
row, col = map(int, input().split())
# 잘라야하는 점선의 개수
N = int(input())

data_list = []
# 자를 점선 입력
for _ in range(N):
    data_list.append(tuple(map(int, input().split())))
print(data_list)

