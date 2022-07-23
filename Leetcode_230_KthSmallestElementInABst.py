#Input: root = [3,1,4,null,2], k = 1
#Output: 1
# Python solution with In Order Traversal by Cracking FAANG T:O(N) S:O(N)

def smallestKth(root,k):
  res = []
  
  while True:
    while root:
      res.append(root)
      root = root.left
      
    root = res.pop()
    k -=
    
    if not k:
      return root.val
    
    root = root.right
 

def smallestKth(root,k):
  res = []
  
  def inorder(node):
    
    inorder(node.left)
    res.append(node.val)
    inorder(node.right)
    

  inorder(root)
  return res[k-1]
