n = int(input())
data = []
for _ in range(n):
    data.append(input().split())

for i in range(n):
    num = int(data[i][0])
    str = data[i][1]
    for s in str:
        print(s*num, end='')
    print()
