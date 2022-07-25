# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Python solution with Stack T:O(N) S:O(N)

def sol(root):
  if not root:
    return []
  
  stack = []
  res = []
  
  while True:
    while root:
      stack.append(root)
      root= root.left
    if stack not None:
      
      root = stack.pop()
      res.append(root.val)
      root = root.right
    else:
      return res
