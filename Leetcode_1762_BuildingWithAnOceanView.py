# input: buildingsHeight = [4,2,3,1]
# output: ([(0, 1), (2, 2), (3, 1)])

# Python Solution with Deque T: O(N) S: O(N)

def viewBuilding(buildingsHeight):
  
  res = collections.dequeu([])
  
  maxHeight = 0
  
  for idx in range(len(buildingsHeight) - 1, -1, -1):
    currHeight = buildingsHeight[idx]
    
    if currHeight > maxHeight:
      
      diffHeight = currHeight - maxHeight
      
      res.appendleft((idx,diffHeight))
      
      maxHeight = currHeight
  
  return res
       
  
