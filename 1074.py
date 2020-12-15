# 배열을 2*2가 될 때 까지 자른 후 입력받은 r, c과 일치하는지 확인하는 방법, 모든 2*2를 하나씩 확인 - 시간초과
'''
N, r, c = map(int, input().split())
count = 0
def divide(size, x, y):
    new_size = size/2
    global count
    if size <= 2:
        if x == r and y == c:
            print(count)
            return
        count += 1
        if x + 1 == r and y == c:
            print(count)
            return
        count += 1
        if x == r and y+1 == c:
            print(count)
            return
        count += 1
        if x + 1 == r and y + 1 == c:
            print(count)
            return
        count += 1
        return
    divide(new_size, x, y) # 2사분면
    divide(new_size, x, y+new_size) # 3사분면
    divide(new_size, x+new_size, y) # 1사분면
    divide(new_size, x+new_size, y+new_size) # 4사분면

divide(2**N, 0, 0)
'''

# 입력받은 r과 c가 어느 사분면에 있는지 확인하면서 나머지는 다 버리는 방법

N, r, c = map(int, input().split())

def divide(size, r, c):
    idx = 0
    if size == 2:
        return r * 2 + c * 1
    half = size // 2
    if r < half and c < half:
        return idx + divide(half, r, c)
    elif r < half and c >= half:
        idx += int(size * size / 4)
        return idx + divide(half, r, c-half)
    elif r >= half and c < half:
        idx += int(size * size / 4 * 2)
        return idx + divide(half, r-half, c)
    else:
        idx += int(size * size / 4 * 3 )
        return idx + divide(half, r-half, c-half)

print(divide(2**N, r, c))