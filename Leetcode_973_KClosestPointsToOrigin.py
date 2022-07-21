#Input: points = [[1,3],[-2,2]], k = 1
#Output: [[-2,2]]
#Explanation:
#The distance between (1, 3) and the origin is sqrt(10).
#The distance between (-2, 2) and the origin is sqrt(8).
#Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
#We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# Python solution with sort O(N*logk)

def closest(points,k):
  
  def euc(point):
    return point[0]**2 + point[1]**2
  
  points.sort(key=euc)
  
  return points[:k]

# Python solution with heap - Max Heap O(N*logk)

def closest(points,k):
  
  heap = []
  
  for (x,y) in points:
    dist = -(x*x+y*y) # normally at python we can not implement max heap so we implement min heap. Meanwhile we need max heap solution to get kth closest points so -dist reverse min heap to max
    if len(heap) == k:
      heapq.heappushpop(heap,(dist,x,y))
    else:
      heapq.heappush(heap,(dist,x,y))
      
  return [(x,y) for (dist,x,y) in heap]
    
