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

arr = [0,0,0]
print(secondlargest(arr))
