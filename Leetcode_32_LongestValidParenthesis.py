# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Python solution with Stack T:O(N) S:O(N)

def sol(s):
  
  res = 0
  stack =[0]
  
  for i in range(len(s)):
    if s[i] == "(":
      stack.append(0)
    else:
      if len(stack) > 1:
        val = stack.pop()
        stack[-1] += val + 2
        res = max(res,stack[-1])
      else:
        stack = [0]
        
  return res
      
