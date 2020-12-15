#최대값 - 3m 49s
'''
nums = []
for _ in range(9):
    nums.append(int(input()))

max_num = max(nums)
for i in range(len(nums)):
    if nums[i] == max_num:
        print(nums[i])
        print(i+1)
'''


nums = []
for _ in range(9):
    nums.append(int(input()))
max_num = max(nums)
print(max_num)
print(nums.index(max_num)+1)



















