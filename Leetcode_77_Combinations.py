#Given two integers n,k return all possible combinations of k numbers out of the range
#Input: n=4, k=2 Output: [[1,4],[1,3],[1,2],[2,3],[2,4],[3,4]]

#Python Solution from Neetcode / Backtracking

def combinations(n,k):
  res = []
  
  def backtrack(remains,comb,nex):
    if remains == 0:
      res.append(comb.copy())
    else:
      for i in range(nex,n+1):
        comb.append(i)
        backtrack(remains-1,comb,i+1)
        comb.pop()
   
   backtrack(k,[],1)
   return res
     
