class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_set = set(ransomNote)
        magazine_set = set(magazine)
        for i in note_set:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
        
"
