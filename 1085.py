# 직사각형에서 탈출 - 2m 13s

x, y, w, h = map(int, input().split())

print(min(x, w-x, y, h-y))
