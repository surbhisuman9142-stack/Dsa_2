def subsets(nums):
    result = []
    path = []
    def backtrack(i):
        if i == len(nums):
            result.append(path[:])
            return
        #choice 1: include nums[i]
        path.append(nums[i])
        backtrack(i+1)
        #undo the choice
        path.pop()
        #choice 2:skip nums[i]
        backtrack(i+1)
    backtrack(0)
    return result
print(subsets([1,2]))