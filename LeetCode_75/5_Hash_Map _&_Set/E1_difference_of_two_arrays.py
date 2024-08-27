nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
# expected output: [[1,3],[4,6]]
nums3 = set()
for i in nums1:
    if i not in nums2:
        nums3.add(i)
nums4 = set()
for i in nums2:
    if i not in nums1:
        nums4.add(i)
print([list(nums3), list(nums4)])


# alternate working solution:

def removeDuplicates(num1, num2):
    res = set()
    for i in num1:
        if i not in num2:
            res.add(i)
    return list(res)

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
print([removeDuplicates(nums1, nums2) , removeDuplicates(nums2, nums1)])
