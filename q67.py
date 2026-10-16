nums = [2,1,5,3,4]
stack = []
result = [-1] * len(nums)
for  i in range(len(nums)):
    while stack and nums[i] > nums[stack[-1]]:
        index = stack.pop()
        result[index] = nums[i]
    stack.append(i)
print(result)