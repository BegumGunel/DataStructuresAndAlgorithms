#Input: root = [1,2,3,4,5,6]
#Output: 110
#Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

# Pyton solution with DFS by Cracking FAANG T: O(N) S: O(N)

def maxProduct(root):
  if not root:
    return 0
  
  tree_sum = []
  
  def dfs(node):
    if not node:
      return 0
    
    l_sum = dfs(node.left)
    r_sum = dfs(node.right)
    
    curr_sum = l_sum + r_sum + node.val
    tree_sum.append(curr_sum)
    
    return curr_sum
  
  total_sum = dfs(root)
  max_product = 0
  
  for sum_ in tree_sum:
    max_product = max(max_product, sum_ * (total_sum - sum_))
    
  return max_product % (10**9 + 7)

    
