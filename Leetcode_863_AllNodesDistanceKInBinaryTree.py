# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
# Python solution with DFS

def distanceK(root,target,k):
  
  def turnToGraph(node,parent):
    if not node:
      return 
    
    node.parent = parent
    turnToGraph(node.left,node)
    turnToGraph(node.right,node)
    
   
  turnToGraph(root,None)
  res = []
  visited = set()
  
    def travGraph(node,distance):
      if not node or distance > k or node in visited:
        return 
      visited.add(node)
      
      if k == distance:
        res.append(node.val)
        return
            
      travGraph(node.parent,distance + 1)
      travGraph(node.left,distance + 1)
      travGraph(node.right, distance + 1)
      
    
  travGraph(target,0)
  return res
  
