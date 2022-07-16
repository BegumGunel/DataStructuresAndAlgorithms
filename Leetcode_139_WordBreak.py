# Input: s = "leetcode", wordDict = ["leet","code"] Output: true

# Python solution with Dynamic Programing

def wordBreak(s,wordDict):
  
  dp = [False] * (len(s) + 1)
  
  for i in range(len(s)):
    for j in range(i,len(s)):
      if dp[i] and s[i:j+1] in wordDict:
        dp[j+1] = True
  
  return dp[-1]


# Python solution with BFS

def wordBreak(s,wordDict):
  
  queue = [s]
  seen = set()
  
  while queue:
    word = queue.pop()
    
    if word in wordDict:
      continue
    else:
      if not word:
        return True
      seen.add(word)
      
    for startword in wordDict:
      if word.startswith(startword):
        queue.append(s[len(startword):]
                     
                     
  return False
      
  
