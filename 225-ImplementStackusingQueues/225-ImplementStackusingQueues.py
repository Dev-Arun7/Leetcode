
    def __init__(self):
        

    def push(self, x: int) -> None:
        

    def pop(self) -> int:
        

    def top(self) -> int:
        

    def empty(self) -> bool:
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
        self.q = deque()
        self.q.append(x)
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()
        return self.q[-1]
        return len(self.q) == 0
# param_4 = obj.empty()
class MyStack:
[
