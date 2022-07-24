# input gas = [5,1,2,3,4]  costs = [4,4,1,5,1] output: 4

# Python Solution with iterative way by Cracking FAANG T:O(N) S:O(1) 

def sol(gas,costs):
  
  total_gas = curr_gas = starting_station = 0
  
  for i in range(len(gas)):
    total_gas += gas[i] - costs[i]
    curr_gas += gas[i] - costs[i]
    
    if curr_gas < 0:
      starting_station = i + 1
      curr_gas = 0
      
  return starting_station if total_gas >= 0 else -1 
     
