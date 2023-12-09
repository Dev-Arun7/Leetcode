class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        
        l = len(nums)
        k = l
        for i in range(l-1,-1,-1):
            if nums[i] == val:
                nums.remove(nums[i])
                k-=1
        return k
