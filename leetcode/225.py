class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)
        while self.queue2:
            self.queue1.append(self.queue2[0])
            self.queue2 = self.queue2[1:]
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        res = self.queue2[0]
        self.queue2 = self.queue2[1:]
        return res

    def top(self) -> int:
        return self.queue2[0]

    def empty(self) -> bool:
        if not self.queue1 and not self.queue2:
            return True
        return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
