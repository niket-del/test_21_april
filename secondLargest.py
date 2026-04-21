def secondlargest(arr):
    count1 = float('-inf')
    count2 = float('-inf')
    for ele in arr:
        if ele > count1:
            count2 = count1
            count1 = ele
        elif ele > count2 and ele != count1:
            count2 = ele
    return count2

arr = [10,20,30,40,50]
print(secondlargest(arr))
