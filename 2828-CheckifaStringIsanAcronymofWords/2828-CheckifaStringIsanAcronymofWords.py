class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acronym = ''.join([i[0] for i in words])
        return s == acronym
        acronym = ''
        
[
