        for i in range(1, l-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                result = i
        if status:
                status = True
        else:
            return result            
            value = max(nums[0], nums[-1])
            return nums.index(value)
        
[
