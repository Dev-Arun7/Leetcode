class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        c=0
        for i in range(k,len(s)+1):
            x=int(s[i-k:i])
            if x!=0 and num%x==0:
                c+=1
        return c
        
2
