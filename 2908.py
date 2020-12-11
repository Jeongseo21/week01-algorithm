a, b = input().split()

for i in range(2, -1, -1):
    if a[i] == b[i]:
        continue
    elif a[i] > b[i]:
        print(a[::-1])
        break
    else:
        print(b[::-1])
        break

