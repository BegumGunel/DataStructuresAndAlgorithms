# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Python solution with BFS == Level Order Traversal T: O(N) S: O(N)

def sol(root):
  
  if not root : return []
  
  res = []
  
  queue = collections.deque([root])
  
  while queue:
    items = []
    
    
    for _ in range(len(queue)):
      
      curr = queue.popleft()
      
      items.append(curr.val)
      
      if curr.left:
        queue.append(curr.left)
      
      if curr.right:
        queue.append(curr.right)
      
    res.append(items)
  return res
      
