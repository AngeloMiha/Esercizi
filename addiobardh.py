def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1.pop(-1)
    
    for i in range(n):
        nums1.append(nums2[i])
    
    nums1 = sorted(nums1)
    return nums1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)
