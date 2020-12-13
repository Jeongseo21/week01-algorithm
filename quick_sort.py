# quick_sort를 만들어보자
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




