# 윤년 - 1m 50s

num = int(input())

if (num % 4 == 0 and num % 100 != 0) or num % 400 == 0:
    print(1)
else:
    print(0)