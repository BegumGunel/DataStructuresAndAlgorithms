#operations = ["5","-2","4","C","D","9","+","+"]
def sol(operations):
  
  newList = []
  
  for op in operations:
    if op == 'C':
      newList.pop()
    elif op == 'D':
      newList.append(newList[-1] * 2)
    elif op == '+':
      newList.append(newList[-2] + newList[-1])
    else:
      newList.append(int(op))
  
  return sum(newList)
      
