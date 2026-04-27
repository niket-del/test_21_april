def removeDuplicates(nums):
    ans = []
    for ele in nums:
        if ele not in ans:
            ans.append(ele)
    return ans


nums = [1, 2, 3, 4, 1, 2, 3, 5]
print(removeDuplicates(nums))