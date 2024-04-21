        num_arr = [int(num) for num in str_digit]
        for i in range(l):
            j = i + 1
            while j < l:
                if num_arr[i] % 2 == num_arr[j] % 2:
                    if num_arr[j] > num_arr[i]:
                        num_arr[j], num_arr[i] = num_arr[i], num_arr[j]
        ans = ''.join(str(num) for num in num_arr)
        return int(ans)
                j += 1

class Solution:
    def largestInteger(self, num: int) -> int:
        ans = ''
        str_digit = str(num)
        l = len(str_digit)
1
