# input: root = [4, 2, 7, 1, 3, 6, 9] 
#output [4,7,2,9,6,3,1]

# Python solution with recursive T:O(N) S:O(N) we do not use any data structure on this problem but becuause of recursive we can count the stack frames otherwise we can define space complextiy O(1)

def invert(root):
  if not root:
    return None
  
  def helper(node):
    if not node:
      return
    
    helper(node.left)
    helper(node.right)
    
    node.left,node.right = node.right,node.left
    
    return node
  
  helper(root)
  return root
