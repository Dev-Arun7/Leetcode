        res = set()

        for i in indices:
            for j in range(len(nums)):
                if abs(i-j) <= k:
                    res.add(j)
        
        res = list(res)
        res.sort()

        return res
[
