#Input ["MyStack", "push", "push", "top", "pop", "empty"] [[], [1], [2], [], [], []]
#Output [null, null, null, 2, 2, false]

Class MyStack:
  
  def __init__(self):
    myStack = deque()
    
  def push(self,x:int) -> None:
    self.myQueue.append(x)
    
  def pop(self) -> int:
    
    for i in range(len(self.myQueue)-1):
      self.myQueue.append(self.myQueue.popleft())
    
    return self.myQueue.popleft()
  
  def top(self) -> int:
    return self.myQueue[-1]
  
  def empty(self) -> bool:
    return len(self.myQueue) == 0
