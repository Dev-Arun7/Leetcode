class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for n in logs:
            if n == "../":
                if count > 0:
            elif n == "./":
                continue
            else:
                count += 1
    
        return count
                    count -= 1
        
[
