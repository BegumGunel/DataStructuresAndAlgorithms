# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

#Python solution with HashMap or Boyer Moore

def sol(nums):
  numbers = {}
  result = 0
  maxNum = 0
  
  for num in nums:
    numbers[num] = 1 + numbers.get(num,0)
       
    if numbers[num] > maxNum:
      result = num 
        
    maxNum = max(maxNum,numbers[num]
  return result
                 
def boyerMoore(nums):
   result = 0
   count = 0
   
   for num in nums:
      if count == 0:
          result = num
      count += 1 if num == result else -1
   
   return result
     
                 
                 
                 

                 
                
