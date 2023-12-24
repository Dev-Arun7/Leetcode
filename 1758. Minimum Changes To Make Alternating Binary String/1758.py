class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0
        count2 = 0
        for i, num in enumerate(s):
            if i % 2 == 0:
                if num != '0':
                    count1 += 1
                if num != '1':
                    count2 += 1
            else:
                if num != '1':
                    count1 += 1
                if num!= '0':
                    count2 += 1
        return min(count1, count2)

        