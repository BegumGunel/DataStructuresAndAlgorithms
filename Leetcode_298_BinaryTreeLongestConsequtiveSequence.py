# Pyton solution by Cracking FAANG T:O(N) S:O(N) if we consider the DFS's counts of stack frames otherwise O(1)

def longestConsequtive(root):
  if not root:
    return 0
  
  longest_path = 1
  
  def dfs(curr_node,prev_node,curr_length,longest_path):
    if curr_node:
      if curr_node.val - 1 == prev_node.val:
        curr_length += 1
        longest_path = max(longest_path,curr_length)
        dfs(node.left,curr_node.val,curr_length)
        dfs(node.right,curr_node.val,curr_length)
      else:
        dfs(node.left,curr_node.val,1)
        dfs(node.right,curr_node.val,1)
    return longest_path
  
  dfs(root,root.val-1,0,longest_path)
  
  return longest_path
