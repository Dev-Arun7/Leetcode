        l = len(s)
        for i in range(l):
                s_letter = s[i]
                t_letter = t[i]
                for j in range(i, l):
                    if s[j] == s_letter:
                        if t[j] != t_letter:
                            return False
                    elif s[j] != s_letter:
                        if t[j] == t_letter:
                            return False
        return True 
        letters = set()
        l2 = len(t)
        if l != l2:
            return False
            if s[i] not in letters:
                    
                letters.add(s[i])
    def isIsomorphic(self, s: str, t: str) -> bool:
        
"
