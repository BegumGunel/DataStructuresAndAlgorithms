# Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
# Output: 1

# Python solution with BFS by Cracking FAANG T: O(N) + O(N) -> 2N -> O(N) S: O(N) + O(N) -> 2N -> O(N)

def timeNeed(n,headID,manager,informTime):
  
  if n <= 1:
    return 0
  
  needTime = 0
  
  connectedDict = collections.defaultDict(list)
  
  for idx,emp in enumerate(manager):
    connectedDict[emp].append(idx)
    
  queue = collections.dequeu([(headID,informTime[headID])])
  
  while queue:
    cur_emp, cur_time = queue.popleft()
    
    needTime = max(needTime,cur_time)
    
    for subEmployees in connectedDict[cur_emp]:
      queue.append((subEmployees,cur_time + informTime[subEmployees]))
      
  
  return needTime
                
                              
                              
