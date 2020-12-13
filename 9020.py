# 숫자 N을 입력받기
N = int(input())

# 1-N까지의 소수 구하기
def prime_nums(N):
    array = []
    for i in range(2, N):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                count += 1
                continue
        if count == i-2:
            array.append(i)
    return array

# 두개를 선택해서 N이 나오는지 확인하기
array = prime_nums(N)
answer_list = []
for i in range(len(array)):
    for j in range(i, len(array)):
        if array[i] + array[j] == N:
            answer_list.append((array[i], array[j]))
# print(answer_list)
answer = answer_list[-1]

print(str(answer[0]) + " " + str(answer[1]))






