class Solution:
    def interpret(self, command: str) -> str:
        temp = command.replace("()", "o") 
        result = temp.replace("(al)", "al")
        return result

"
