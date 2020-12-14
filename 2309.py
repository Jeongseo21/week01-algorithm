nji=[]
flag = [True]*9

for _ in range(9):
    nji.append(int(input()))
    nji = sorted(nji)

for i in range(9):
    for j in range(i+1, 9):
        if sum(nji) - (nji[i] + nji[j]) == 100:
            flag[i] = False
            flag[j] = False
            break

        else:
            continue
    if False in flag:
        break


for i in range(9):
    if flag[i]:
        print(nji[i])
