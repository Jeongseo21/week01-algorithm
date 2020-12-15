# OX퀴즈 -

'''
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
'''






flag = False
num = int(input())
cases = []
for _ in range(num):
    cases.append(input())


for case in cases:
    result, count = 0, 0
    for s in case:
        if flag == False:
            if s == 'O':
                flag = True
                count = 1
                result += count
        else:
            if s == 'O':
                count += 1
                result += count
            else:
                flag = False
    print(result)
















