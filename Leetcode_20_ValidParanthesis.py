# Input: s = "()[]{}"
# Output: true
# Python solution with Stack and Dictionary T:O(N) S:O(N) + O(N) -> 2N -> O(N)

def sol(s):
  
  bracketDict = {")":"(","]":"[","}":"{"}
  stack = []
  
  if s[0] in ["}","]",")"] or if s[-1] in ["(","[","{"]:
    return false
  
  for ch in s:
    if ch in ["(","[","{"]:
      stack.append(ch)
    else:
      if stack[-1] == bracketDict[ch]:
        stack.pop()
  
  
  return len(stack) == 0
      
