import itertools

# nPn 순열 구하기 - 순열/조합 구하는 알고리즘 공부
n = int(input())
arr = list(map(int, input().split()))
nPr = itertools.permutations(arr, len(arr))
arrays = list((nPr))
answer = []
for array in arrays:
    result = 0
    for i in range(1, len(array)):
        result += abs(array[i]-array[i-1])
    answer.append(result)
print(max(answer))