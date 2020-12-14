
# 런타임 에러가 발생하면 배열의 길이를 잘못 선언했는지 확인하기

N = int(input())
words = []

# 단어 입력하기
for _ in range(N):
    words.append(input())
# 중복 제거하기
words = set(words)

# 길이를 저장하는 배열 선언
length = [None]*1000

# 단어가 저장된 단어의 길이에 해당하는 인덱스에 저장
for w in words:
    l = len(w)
    if length[l]:
        length[l].append(w)
    else:
        length[l] = [w]

# None이 아닐 경우 정렬해주기
for i in range(len(length)):
    if length[i]:
        length[i].sort()

# None이 아닐 경우 출력해주기
for i in range(len(length)):
    if length[i]:
        for j in range(len(length[i])):
            print(length[i][j])