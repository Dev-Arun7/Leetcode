
        l = len(nums)
        window_sum = sum(nums[:k])
        left = 0
        right = k
        #     max_avg = max(max_avg, current_sum / k)
        # return max_avg
        max_sum = window_sum
        while right < l:
            window_sum += nums[right]
            window_sum -= nums[left]
            left += 1
            right += 1
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k


        #     current_sum += nums[i] - nums[i - k]
[
