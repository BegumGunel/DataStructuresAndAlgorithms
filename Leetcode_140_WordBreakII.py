#Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
#Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

# Python solution with DFS + Backtracking
# Backtraking VS DFS : both algorithms implementation are so similar although dfs goes deep, backtrack goes deep with constraints so search space limited. 
# Backtrack more efficent for space complexity beacuse of the search space, you can use it on puzzles espacially to find all possibilies of result.
# On the other hand DFS find one solution. 


def wordBreak2(s,worDict):
  res =[]
  
  def dfs(idx,path):
    if len(s) == idx:
      res.append(" ".join(path))
     
    for i n range(idx,len(s)):
      tmp = s[idx:i+1]
      if tmp in wordDict:
        dfs(idx+1,path + [tmp])
  
  dfs(0,[])
  return res
