def removeElement(nums,value):
    for element in nums:
        if element == value:
            nums.remove(element)
    return nums

nums = [5,7,12,15,12,19]
value = 12
print(removeElement(nums,value))

#currently it remove all the matching values from array


def removeElement(nums,value):
    for element in nums:
        if element == value:
            nums.remove(element)
            return nums

# the above code remove only first value




nums = [5,7,12,15,12,19]
value = 12
print(removeElement(nums,value))