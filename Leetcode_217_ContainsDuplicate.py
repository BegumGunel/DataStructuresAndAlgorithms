# Input: nums = [1,2,3,1]
# Output: true

# Python solution T: O(N) S: O(N)

def sol(nums):
  return len(nums) != len(set(nums))
