class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash = {}
        for num in arr:
            if 2 * num in hash or num / 2 in hash:
                return True
            else:
                hash[num] = True
        return False
        
[
