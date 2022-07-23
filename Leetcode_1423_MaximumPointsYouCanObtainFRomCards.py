# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However,
# choosing the rightmost card first will maximize your total score. 
# The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

# Python Solution with Window Sliding by Cracking FAANG T: O(N) S: O(1)

def maxiPoint(cardPoints,k):
  
  ans = 0
  curr = 0
  
  for i in range(-k,k):
    curr += cardPoints[i]
    
    if i >= 0:
      curr -= cardPoints[i-k]
      
    ans = max(ans,curr)
  
  return ans
      
