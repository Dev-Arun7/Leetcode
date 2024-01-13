class Solution:
    def minLength(self, s: str) -> int:
        status = True
        new = s
        while status:
            if 'AB' in new or 'CD' in new:
                new = new.replace('AB', '')
                new = new.replace('CD', '')
            else:
                status = False
        return len(new)
        
"
