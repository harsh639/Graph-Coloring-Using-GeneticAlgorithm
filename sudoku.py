board = []
for i in range(1, 74, 9):
   row = []
   for j in range(i, i+9):
       row.append(j)
   board.append(row)
for l in board:
   print(l)
squares = []
for i in range(1, 8, 3):
   for k in range(1, 8, 3):
       square = []
       for j in range(i, i+3):
               for l in range(k, k+3):
                   square.append(board[j-1][l-1])
       squares.append(square)
for l in squares:
   print(l)
sudoku = []
for i in range(81):
   row = []
   for j in range(81):
       row.append(0)
   sudoku.append(row)
for l in sudoku:
   print(l)
Adj = []
for i in range(1, 82):
   row = (i-1)//9
   column = (i-1)%9
   adj = []
   for j in range(9):
       adj.append(board[row][j])
   for j in range(9):
       adj.append(board[j][column])
   row_block = row//3
   column_block = column//3
   square_number = row_block*3 + column_block
   for j in squares[square_number]:
       adj.append(j)
   Adj.append(adj)
for l in Adj:
   print(l)
for i in range(81):
   for j in Adj[i]:
       print(i, j-1)
       sudoku[i][j-1] = 1
for i in range(81):
   sudoku[i][i] = 0
for l in sudoku:
   print(l)