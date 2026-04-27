def removeEmelentUsingIndex(nums,index):
    nums.pop(index)
    return nums

nums = [5,7,12,15,12,19]
index = 1
print(removeEmelentUsingIndex(nums,index))