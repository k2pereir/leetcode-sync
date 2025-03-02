class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)): 
            if nums[i] == val: 
                print(nums[i])
                nums[i] = "_"
            else: 
                k += 1
        nums.sort()
        return k

