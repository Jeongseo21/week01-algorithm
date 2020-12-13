

def recur(n:int)->int:
    s = []

    while True:
        if n > 0:
            s.append(n)
            n = n-1
            continue
        if len(s) != 0:
            n = s.pop()
            print(n)
            n = n - 2
            continue
        break

recur(4)