# Given an array nums of distinct integers, return all the possible permutations
# Input: nums=[1,2,3] Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

#Pyton Solution from neetcode / Backtracking

def permutations(nums):
  res = []
  def backtrack(perm):
    if len(nums) == len(perm):
      res.append(perm.copy())
      return
    
    for i in nums:
      if not i in perm:
        perm.append(i)
        backtrack(perm)
        perm.pop()
        
  backtrack([])
  return res
  
