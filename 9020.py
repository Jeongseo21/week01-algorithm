'''
# 시간초과

# 숫자 N을 입력받기
N = int(input())
nums = [0]*N

for _ in range(N):
    nums[_] = int(input())

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

# 두개를 선택해서 num이 나오는지 확인하기
def answer(array, num):
    answer_list = []
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] + array[j] == num:
                answer_list.append((array[i], array[j]))
    # print(answer_list)
    answer = answer_list[-1]

    print(str(answer[0]) + " " + str(answer[1]))

for num in nums:
    # print(num)
    array = prime_nums(num)
    answer(array, num)
'''

# 숫자 N을 입력받기
N = int(input())
nums = [0]*N

for _ in range(N):
    nums[_] = int(input())

# 1-N까지의 소수 구하기
def prime_nums(N):
    prime = []

    prime.append(2)

    for n in range(3, N+1, 2):
        for i in range(0, len(prime)):
            if n % prime[i] == 0:
                break
        else:
            prime.append(n)

    return prime

# 두개를 선택해서 num이 나오는지 확인하기
def answer(array, num):
    answer_list = []
    for i in range(len(array)-1, -1, -1):
        for j in range(len(array)-1, i-1, -1):
            if array[i] + array[j] == num:
                answer_list.append((array[i], array[j]))
                break
        if len(answer_list) == 1:
            break
    # print(answer_list)
    answer = answer_list[0]

    print(str(answer[0]) + " " + str(answer[1]))

for num in nums:
    array = prime_nums(num)
    # print(array)
    answer(array, num)


