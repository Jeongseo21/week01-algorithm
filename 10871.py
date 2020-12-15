# N보다 작은 수 - 2m 5s

N, X = map(int, input().split())

nums = list(map(int, input().split()))

for n in nums:
    if n < X :
        print(n, end=' ')