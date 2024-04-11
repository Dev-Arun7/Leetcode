class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                else:
                        stack.pop()
            return ''.join(stack)

        return build_string(s) == build_string(t)
                    if stack:
        
"
