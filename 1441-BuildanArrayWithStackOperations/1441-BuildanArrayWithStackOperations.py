class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l = len(target)
        stack = []
        curr = 0
        for i in range(1, n+1):
            if target[curr] == i:
                stack.append("Push")
            else:
                stack.append("Push")
                stack.append("Pop")

                curr += 1
        return stack
            if target[-1] == i:
                break
        
[
