class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k < numOnes:
            return k
        elif k < numOnes + numZeros:
            return numOnes
        else:
            rem = k - (numOnes + numZeros)
            return numOnes - rem
3
