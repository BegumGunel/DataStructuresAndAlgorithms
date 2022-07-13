# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string. Return the list all possible strings
#Inpu: s="1ab2" Output: ["1ab2","1Ab2","1aB2","1AB2"]

#python solution by neetcode / Backtracking

def letterCasePermutation(s):
  res = []
  def backtrack(idx,perm):
    if len(perm) == len(s):
      res.append("".join(perm.copy()))
      return
    
    if s[idx].isalpha():
      perm.append(s[idx].lower())
      backtrack(idx+1,perm)
      perm.pop()
      perm.append(s[idx].upper())
      backtrack(idx+1,perm)
      perm.pop()
    else:
      perm.append(s[idx])
      backtrack(idx+1,perm)
      perm.pop()
      
  backtrack(0,[])
  return res
