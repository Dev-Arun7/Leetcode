            else:
                groups[ref_hash[_sum]].append(num)  # Access groups using index
        
        length = 0
        count = 0
        for i in groups:
            if len(i) > length:
                length = len(i)
                count = 1
            elif len(i) == length:
                count += 1
                groups.append([num])
            _sum = sum(int(digit) for digit in str_num)
            if _sum not in ref_hash:
                ref_hash[_sum] = len(groups)  # Store index instead of number
        ref_hash = {}
        for num in range(1, n + 1):
            str_num = str(num)
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = []
1
