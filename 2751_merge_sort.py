'''
# 병합정렬 merge sort 구현 - 에러
result = []
# 정복
def conquer(array, start, mid, end):
    global result
    i = start # 왼쪽 정렬 시작 인덱스
    j = mid+1 # 오른쪽 정렬 시작 인덱스
    k = 0 # result의 인덱스

    # 왼쪽 정렬과 오른쪽 정렬 비교
    while(i <= mid and j <= end):
        if array[i]<=array[j]:
            result.append(array[i])
            i += 1
            k += 1
        else:
            result.append(array[j])
            j += 1
            k += 1
    # 왼쪽이 살아있다면
    while(i <= mid):
        result.append(array[i])
        i += 1
        k += 1
    # 오른쪽이 살아있다면
    while(j <= end):
        result.append(array[j])
        j += 1
        k += 1
    print(result)


# 분할
def divide(array, start, end):
    if start < end:
        mid = (end + start)//2

        divide(array, start, mid)
        divide(array, mid+1, end)

        conquer(array, start, mid, end)
    # 탈출 조건
    else:
        return

divide([4, 8, 9, 6, 5, 1, 3, 2], 0, 7)
'''
def merge_sort(a):
    def re_merge_sort(a, left, right):
        if left < right:
            mid = (left + right) //2

            re_merge_sort(a, left, mid)
            re_merge_sort(a, mid+1, right)

            p = j = 0
            i = k = left

            while i <= mid:
                buff[p] = a[i]
                p += 1
                i += 1
            while i <= right and j<p:
                if buff[j] < a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1
            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None]*n
    re_merge_sort(a, 0, n-1)
    del buff

a = []
N = int(input())
for _ in range(N):
    a.append(int(input()))
merge_sort(a)
for _ in a:
    print(_)