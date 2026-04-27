def removeEmelentUsing(nums,index,element):
     nums.insert(index,element)
     return nums

nums = [5,7,12,15,12,19]
index = 1
element = 11
print(removeEmelentUsing(nums,index,element))