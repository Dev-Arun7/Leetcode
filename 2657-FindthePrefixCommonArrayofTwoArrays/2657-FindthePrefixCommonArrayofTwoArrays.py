class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        l = len(A)
        set_A = set()
        set_B = set()
        set_C = set()
        result = []
        for i in range(l):
            set_A.add(A[i])
            set_B.add(B[i])
            set_C = set_A & set_B
            result.append(len(set_C))
            set_C.clear()
        return result
            
[
