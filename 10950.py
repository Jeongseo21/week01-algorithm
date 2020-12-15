# A+B -3

N = int(input())
cases = []
for _ in range(N):
    cases.append((tuple(map(int, input().split()))))

for i in range(N):
    print(cases[i][0]+cases[i][1])