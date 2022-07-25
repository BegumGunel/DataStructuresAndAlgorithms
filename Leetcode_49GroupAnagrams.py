#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# python solution with Dict by Cracking Faang T:O(N) * O(K) -> K length of the longest string S:O(NK)

for sol(strs):
  
  groups = collections.defaultdict(list)
  
  for word in strs:
    chars = [0] * 26
    
    for ch in word:
      chars[ord(ch) - ord('a')] += 1 
      
    groups[tuple(chars)].append(word)
    
   return groups.values()
      
    
