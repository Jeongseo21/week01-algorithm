# 가로길이 col, 세로길이 row
r, c = map(int, input().split())
# 잘라야하는 점선의 개수
N = int(input())

# row, col 자르는 곳 저장
row = [0, c]
col = [0, r]

# 자를 점선 입력
for _ in range(N):
    way, num = map(int, input().split())
    if way == 0:
        row.append(num)
    else:
        col.append(num)

# 입력 받은 방법을 크기 순서대로 sort
row.sort()
col.sort()

list_w = []
list_h = []

for i in range(len(row)-1):
    list_w.append(row[i+1]-row[i])
for i in range(len(col)-1):
    list_h.append(col[i+1]-col[i])

ans = -1
for i in list_w:
    for j in list_h:
        if i*j > ans:
            ans = i*j
print(ans)





