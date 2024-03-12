class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice = sum(aliceSizes)
        bob = sum(bobSizes)
        half = (alice + bob) // 2
        for i in aliceSizes:
            if half - (alice - i) in bobSizes:
                return [i, half - (alice - i)]

[
