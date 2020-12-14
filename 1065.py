N = int(input())

if N < 100:
    hansoo = N
elif N == 1000:
    hansoo = 144
else:
    hansoo = 99
    for i in range(100, N+1):
        if int(str(i)[0])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[2]):
            hansoo += 1
print(hansoo)