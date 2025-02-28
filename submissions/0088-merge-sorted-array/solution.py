class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[len(nums1) - 1 - i] = nums2[i]
        nums1.sort()
        
