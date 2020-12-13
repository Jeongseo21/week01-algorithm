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
    divide(new_size, x, y)
    divide(new_size, x, y+new_size)
    divide(new_size, x+new_size, y)
    divide(new_size, x+new_size, y+new_size)

divide(2**N, 0, 0)

'''
if (x+1)/N >1:
    if (y+1)/N >1:
        print("4사분면")
    else:
        print("2사분면")
else:
    if (y+1)/N > 1:
        print("3사분면")
    else:
        print("1사분면")
'''