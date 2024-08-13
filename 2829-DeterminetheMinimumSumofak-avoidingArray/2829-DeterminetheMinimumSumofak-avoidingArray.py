class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        avoiding_set = set()
        sum_ = 0
        i = 1
        while True:
            if k - i not in avoiding_set:
                avoiding_set.add(i)

                sum_ += i
            i += 1
            if len(avoiding_set) == n:
                break
        return sum_
        
5
5
4
2
6
18
3
18
3
