#Input: root = [1,2,3,4,null,2,4,null,null,4]
#Output: [[2,4],[4]]

# Python solution with DFS preOrder traversal T:O(N) we touch every node because of DFS, S: O(N) we are work with dfs so its going to cost O(N) and 
# maintaining visited hash map so it depends on number of elements of the tree so it costs O(N) too O(N) + O(N) -> O(N)

def findDuplicate(root):
  if not root:
    return []
  
  res = []
  visited = {}
  
  def dfs(node,path):
    if not node:
      return '*'
    
    path += ",".join([str(node.val),dfs(node.left,path),dfs(node.right,path)])
    
    if path in visited:
      if visited[path] == 1:
        visited[path] += 1
        if visited[path] == 2:
          res.append(node)
     else:
      visited[path] = 1
      
    return path
  
  dfs(root,'')
  return res
