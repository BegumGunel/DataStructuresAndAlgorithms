# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Python solution with BFS (Level Order Traversal)
# this a linear solution we touch all the nodes so T: O(N) and S:O(N)

def sol(root):
  
  if not root:
    return []
  
  queue = collections.deque([root])
  
  res = []
  
  while queue:
    
    levelOfTree_nodes = len(queue)
    
    for i in range(levelOfTree_nodes):
      
      node = queue.popleft()
      
      if i == levelOfTree_nodes - 1: #last element of queue for that level of tree, this means there is no node on front of that - right side
        res.append(node.val)
      
      if node.left:
        queue.append(node.left)
      
      if node.right:
        queue.append(node.right)
        
  return res
