# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

#Python Solution by me with dfs but unfortunately it returns Time Limit Exceed

def wordSearch(board, word):
    visited = set()

        def check(row, col, remainWord, board, visited):

            if len(remainWord) == 0:
                return True
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for direction in directions:
                row_inc = row + direction[0]
                col_inc = col + direction[1]

                if 0 <= row_inc < len(board) and 0 <= col_inc < len(board[0]) and not (row_inc, col_inc) in visited:
                    if board[row_inc][col_inc] == remainWord[0]:
                        visited.add((row_inc, col_inc))
                        if check(row_inc, col_inc, remainWord[1:], board, visited):
                            return True
                        else:
                            visited.remove((row_inc, col_inc))
            
            return False
        for m in range(len(board)):
            for n in range(len(board[0])):

                if board[m][n] == word[0]:
                    visited.add((m,n))
                    if check(m,n,word[1:],board,visited):
                        return True
                    else:
                        visited.clear()
        return False
      
      
 # Python solution by leetcoders with DFS

def wordSearch(board,word):
  rows = len(board)
  cols = len(board[0])
  visited = set()
  
  def dfs(row,col,index):
    if index == len(word) - 1:
      return True
    if row < 0 or row >= rows or col < 0 or col >= cols or index >= len(word) or board[row][col] != word[index] or (row,col) in visited:
      return False
    
    c1 = dfs(row + 1, col, index + 1)
    c2 = dfs(row - 1, col, index + 1)
    c3 = dfs(row, col + 1, index + 1)
    c4 = dfs(row, col - 1, index + 1)
    
    return c1 or c2 or c3 or c4
  
  for m in range(rows):
    for n in range(cols):
      if board[m][n] == word[0]:
        if dfs(m,n,0):
          return True
  return False

  


      
