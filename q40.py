arr = [1,2,2,3,3,4,5]
result = []
for nums in arr:
    if nums not in result:
     result.append(nums)
print(result)
