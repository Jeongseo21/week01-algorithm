# quick_sort를 만들어보자
'''
백준 시간초과

array = []
N = int(input())
for _ in range(N):
    array.append(int(input()))

def quick_sort(array, left, right):
    n = len(array)
    # 왼쪽 커서
    pl = left
    # 오른쪽 커서
    pr = right
    # 피봇 원소
    pivot = array[(left+right)//2]

    print(f'array[{left}]~array[{right}] :', *array[left:right + 1])

    while pl <= pr:
        while array[pl] < pivot:
            pl += 1
        while array[pr] > pivot:
            pr -= 1
        if pl <= pr:
            array[pl], array[pr] = array[pr], array[pl]
            pl += 1
            pr -= 1
        # print(array[pl], array[pr])
    if left < pr:
        quick_sort(array, left, pr)
    if pl < right:
        quick_sort(array, pl, right)
    #print(array[:pl])
    # print([pivot])
    # print(array[pr+1:])

quick_sort(array, 0, len(array)-1)
for _ in range(N):
    print(array[_])
'''
################################################################
'''
# 퀵정렬 두 번째 구현 방법 - 백준 런타임 에러
array = []
N = int(input())
for _ in range(N):
    array.append(int(input()))

def quick_sort(array, start, end):
    # 원소가 1 개인 경우 종료
    if start >= end:
        return

    # 첫번째 원소를 피봇으로 설정
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left>right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array)-1)
print(array)
'''
####################################################################
# 비재귀적 퀵 정렬
array = []
N = int(input())
for _ in range(N):
    array.append(int(input()))

def quick_sort(array, left, right):
    range = []

    range.append((left, right))

    while not range == []:
        pl, pr = left, right = range.pop() # 왼쪽 오른쪽에 커서 놓기
        pivot = array[(left+right)//2] # 가운데 원소는 피봇으로 설정

        while pl <= pr:
            while array[pl]<pivot:
                pl += 1
            while array[pr]>pivot:
                pr -= 1
            if pl <= pr:
                array[pl], array[pr] = array[pr], array[pl]
                pl += 1
                pr -= 1

        if left < pr:
            range.append((left, pr))
        if pl < right:
            range.append((pl, right))

quick_sort(array, 0, len(array)-1)
for _ in array:
    print(_)
