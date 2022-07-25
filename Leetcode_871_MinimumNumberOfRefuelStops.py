#Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
#Output: 2

# Python solution with heap by Cracking FAANG T:O(NlogK) k is the size of heap S:O(N)

def sol(target,startFuel,stations):
  
  heap =[]
  
  stations.append([target,0])
  
  prev = 0
  refuels = 0
  
  for location,capacity in stations:
    startFuel -= (location - prev)
    
    while heap and startFuel < 0:
      startFuel += heapq.heappop(heap)
      refuels +=1
    
    if startFuel < 0:
      return -1
    
    heapq.heappush(heap,capacity)
    prev = location
  
  return refuels
