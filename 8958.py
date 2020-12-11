n = int(input())
cases = []

for _ in range(n):
    cases.append(input())
count = 0
flag = False

for case in cases:
    result, count = 0, 0
    for s in case:
        if s == 'O':
            if flag is False:
                count = 1
                result += count
                flag = True
            else:
                count += 1
                result += count
        else:
            if flag:
                flag = False
                count = 0
    print(result)
