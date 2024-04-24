
        if right <= l:
            for i in range(right):
                window_sum += nums[i]
        if k < l:    
            while right < l + 1:
                ans.append(window_sum // (2 * k + 1))
                window_sum -= nums[left]
                if right < l:
                    window_sum += nums[right]
                left += 1
                right += 1

        for i in range(l - k, l):
            ans.append(-1)

        return ans
        
            ans.append(-1)
        for i in range(length):
        window_sum = 0
        length = min(k, l)
        left = 0
        right = 2 * k + 1
        ans = []
        l = len(nums)
    def getAverages(self, nums: List[int], k: int) -> List[int]:
class Solution:
            if len(ans) == l:
                return ans

                if len(ans) == l:
                    return ans
            if len(ans) == l:
                return ans
[
