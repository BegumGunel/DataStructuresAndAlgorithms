#Input: nums = [4,1,2,1,2]
#Output: 4

# Python solution with T: O(N) S: O(1)

def sol(nums):
  res = 0
  
  for num in nums:
    res = num ^ res
  
  return res
