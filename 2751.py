N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

def quick(nums, N):
    pivot = nums[N//2]
    right = [x for x in nums if x > pivot]
    left = [y for y in nums if y < pivot]
    return left + [pivot] + right

qlist = quick(nums, N)
for _ in qlist:
    print(_)