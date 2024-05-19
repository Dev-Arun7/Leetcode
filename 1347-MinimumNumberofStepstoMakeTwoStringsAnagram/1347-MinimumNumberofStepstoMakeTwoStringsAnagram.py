            if chr in s_hash:
                s_hash[chr] += 1
            else:
                s_hash[chr] = 1
                t_hash[chr] = 0

        for chr in t:
            if chr in s_hash:
                t_hash[chr] += 1

        for n in s_hash:
            if n in t_hash:
        for chr in s:
        t_hash = {}
        s_hash = {}
    def minSteps(self, s: str, t: str) -> int:
class Solution:

        res = 0

        return res


                if s_hash[n] > t_hash[n]:
                    res += s_hash[n] - t_hash[n]
            else:
                res += s_hash[n]
"
