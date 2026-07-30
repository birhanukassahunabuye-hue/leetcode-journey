class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value: int) -> None:
        
          curr_min = value
          
          if self.minstack:
              curr_min = min(curr_min, self.minstack[-1])
          self.stack.append(value)
          self.minstack.append(curr_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
#obj = MinStack()
#obj.push(value)
#obj.pop()
#param_3 = obj.top()
#param_4 = obj.getMin()