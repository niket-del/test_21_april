def twoSum(nums, target):
    index = {}
    for key, value in enumerate(nums):
        compliment = target - value
        if compliment in index:
            return [index[compliment], key]
        index[value] = key
    else:
        return -1


nums = [7, 2, 11, 15]
target = 20
print(twoSum(nums, target))