#Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

#Python solution with DFS

def concatenatedWords(words):
  visited = set(words)
  res = []
  
  def dfs(w,visited):
    
    for i in range(1,len(w)+1):
      if w[:i] in visited:
        if w[i:] in visited or dfs(w[i:],visited):
          return True
    return False
  
  for word in words:
    if dfs(word,visited):
      res.append(word)
      
  return res
