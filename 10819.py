import itertools

# nPn 순열 구하기 - 순열/조합 구하는 알고리즘 공부
n = int(input())
arr = list(map(int, input().split()))
nPr = itertools.permutations(arr, len(arr))
arrays = list((nPr))
print(arrays)
answer = []
for array in arrays:
    result = 0
    for i in range(1, len(array)):
        result += abs(array[i]-array[i-1])
    answer.append(result)
print(max(answer))

'''
#순열
import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2) # n개 원소 중에 2개를 뽑아 순서를 정해 나열하기
print(list(nPr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

#조합
import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2) # n개의 원소 중에 2개를 뽑기
print(list(nCr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]
'''