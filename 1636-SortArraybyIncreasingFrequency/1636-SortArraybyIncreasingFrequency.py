class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # count = Counter(nums)
        count = {}
        for n in nums:
        def custom_sort(n):
            return (count[n], -n)
        nums.sort(key = custom_sort)
        return nums
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
[
[1,1,2,2,2,3]
[2,3,1,3,2]
[-1,1,-6,4,5,-6,1,4,1]
[3,1,1,2,2,2]
[1,3,3,2,2]
[5,-1,4,4,-6,-6,1,1,1]
[3,1,1,2,2,2]
[1,3,3,2,2]
[5,-1,4,4,-6,-6,1,1,1]
