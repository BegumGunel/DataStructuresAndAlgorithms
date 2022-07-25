# Input: root = [2,1,3]
# Output: true

# Python solution with DFS - POSTORDER(left-right-root) by Cracking FAANG

def sol(root):
  
  def dfs(node):
    if not node:
      return (False,float('inf'),float('-inf'))
    
    if not node.left and node.right:
      return (True,node.val,node.val)
    
    l_ist_BST, l_min, l_max = dfs(node.left)
    r_ist_BST, r_min, r_max = dfs(node.right)
    
    if l_ist_BST and r_ist_BST and l_max < node.val < r_min:
      return (True,l_min,r_max)
    
    elif l_ist_BST and not node.right and node.val > l_max:
      return (True,l_min,node.val)
    elif r_ist_BST and not node.left and node.val < r_min:
      return (True,node.val,r_max)
    else:
      return (False,float('inf'),float('-inf'))
             
  
  return dfs(root)[0]
              
 # Python solution with Stack INORDER(left-root-right)
 
  def sol(root)
  
  stack = []
  pre = None
  
  while True:
    while root:
      stack.append(root)
      root = root.left
    
    if stack = []:
      return True
    root = stack.pop()
    if pre and pre.val >= root.val:
      return False
    
    pre = root
    root = root.right
    
    
      
   
  
  
  
  
  
  
              
              
