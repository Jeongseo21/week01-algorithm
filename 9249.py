'''
# Brute Force : O(n^2 * m) 시간초과

import sys

long_string = sys.stdin.readline()
string = sys.stdin.readline()
# print(len(string))
dict = {}
length = []
for i in range(len(string)):
    for j in range(i, len(string)):
        a = string[i:j+1]
        print(a)
        if a in long_string:
            dict[len(a)] = a
            length.append(len(a))

l = max(length)
print(l)
print(dict[l])
'''
import sys

string = sys.stdin.readline()
target = sys.stdin.readline()
check = []


# 최장 부분 찾기
max_len = 0
for i in range(len(target)):
    check.append([0]*len(string))

    for j in range(len(string)):
        if target[i] != string[j]:
            check[i][j] = 0
        else:
            if target[i] != '\n':
                if i == 0:
                    check[i][j] = 1
                check[i][j] = check[i-1][j-1]+1
                max_len = max(max_len, check[i][j])

# # 문자열 출력
# for i in range(len(target)):
#     for j in range(len(string)):
#         if check[i][j] == max_len:
#             answer = string[j-(max_len-1):j+1]


print(max_len)
# sys.stdout.write(answer)