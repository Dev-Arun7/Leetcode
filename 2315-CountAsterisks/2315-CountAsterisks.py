class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        status = True
        for i in s:
            if status and i == "*":
                count += 1
            if i == "|":
                status = not status
        return count

        
"
