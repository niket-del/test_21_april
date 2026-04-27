def findMaxMin(nums):
    maximum = float('-inf')
    minimum = float('inf')
    for element in nums:
        if element > maximum:
            maximum = element
        if element < minimum:
            minimum = element
    return {'maximum':maximum,'minimum': minimum}

nums = [5,7,12,15,12,19]
print(findMaxMin(nums))
