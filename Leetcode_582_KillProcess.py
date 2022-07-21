# input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5 # [5,10]
# output: [5,10]
# Python solution with BFS T: O(N) + O(N) -> O(2N) -> O(N) S: O(N) + O(N) -> O(2N) -> O(N)

def killProcess(pid,ppid,kill):
  graph = collections.defauldict(list)
  
  for child,parent in zip(pid,ppid):
    graph[parent].append(child) # O(N)
    
  res = []
  queue = collections.deque([kill]) # O(N)
  
  while queue:
    
    killing = queue.popleft()
    res.append(killing)
    
    if killing in graph:
      graph.extend(graph[killing])
  
  return res
    
  
  
