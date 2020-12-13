def hanoi(no):

    if no > 1 :
        return hanoi(no-1) * 2 + 1
    else:
        return 1

def move(no, x, y):
    if no > 1:
        move(no -1, x, 6-x-y)
    print(str(x) +" "+str(y))
    if no > 1:
        move(no - 1, 6 -x-y, y)


N = int(input())
if N > 20:
    print(hanoi(N))
else:
    print(hanoi(N))
    move(N, 1, 3)

'''
def hanoi_under20(no, x, y):

    if no > 1 :
        print(str(x) + " " + str(y))
        return hanoi_under20(no-1, x, 6-x-y) + 1 + hanoi_under20(no-1,6-x-y,y)
    else:
        print(str(x) + " " + str(y))
        return 1
'''