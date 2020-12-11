'''
# 왼쪽 공백 지우기
lstrip()
# 오른쪽 공백 지우기
rstrip()
# 양쪽 공백 지우기
strip()
'''

'''
str = input().strip()
print(str.count(' ')+1)
'''

count = 0
str = input().strip()
for s in str:
    if s == ' ':
        count += 1
print(count+1)