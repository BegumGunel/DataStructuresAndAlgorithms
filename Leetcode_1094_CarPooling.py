# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false

# Python solution with Heap min and sort by Cracking FAANG T:O(NlogN) S:O(N)

def sol(trips,capacity):
  
  trips.sort(key=lambda x: x[1])
  
  heap = []
  
  for trip in trips:
    passanger,start,end = trip
    
    if heap:
      while heap and start >= heap[0][0]:
        _end,_passanger = heapq.heappop(heap)
        
        capacity += _passanger
        
    if passanger > capacity:
      return False
    
    capacity -= passanger
    
    heapq.heappush(heap,[end,passanger])
    
  return True
                   
