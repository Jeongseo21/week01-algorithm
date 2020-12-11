N = int(input())

a = tuple(map(int, input().split()))

answer = 0
for n in a:
    count = 0
    for i in range(2,n):
        if n % i == 0:
            break
        else:
            count += 1
            continue
    if count == n-2:
        answer += 1
print(answer)