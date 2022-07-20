#Input: time = [30,20,150,100,40]
#Output: 3
#Explanation: Three pairs have a total duration divisible by 60:
#(time[0] = 30, time[2] = 150): total duration 180
#(time[1] = 20, time[3] = 100): total duration 120
#(time[1] = 20, time[4] = 40): total duration 60

#Python Solution by Cracking FAANG
#T: O(N) S:O(N)

def sol(durations):
  pairs = 0
  remainDic = collections.defaultdict(int)
  
  for duration in durations:
    if duration % 60 == 0:
      pairs += remainDic[0]
    else:
      pairs += remainDic[60 - (duration % 60)]
    
    remainDic[duration % 60] +=1
   
  return pairs
