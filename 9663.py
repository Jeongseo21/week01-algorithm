N = int(input())
pos = [0]*N
flag = [False]*N
answer = 0
# 출력


def abs_(i):
    count = 0
    if i == 0:
        return True
    else:
        for k in range(i):
            if abs(i - k) == abs(pos[i] - pos[k]):
                break
            else:
                count += 1
                continue
        if count == i:
            return True
        else:
            return False

# i열에 퀸을 배치
def set(i):
    global answer
    # i열 j행에 퀸을 배치
    for j in range(N):
        if not flag[j]:
            pos[i] = j
            if not abs_(i):
                continue
            # 종료조건
            if i == N-1:
                answer += 1
            else:
                flag[j] = True
                # 다음 열의 퀸을 배치
                set(i+1)
                # flag를 False로 돌려놓지 않으면 01234567 한 가지 경우만 출력되고 flag가 모두 True여서 프로그램이 종료됨
                # flag를 False로 돌려놔야 행, 열에 새로운 숫자가 들어갔을 때 다시 flag를 사용할 수 있음
                flag[j] = False

set(0)
print(answer)

