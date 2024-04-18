class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l = len(goal)
        for i in range(l):
            if goal[i : l] + goal[: i] == s:
                 return True
        return False
        
"
