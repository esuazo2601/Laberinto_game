from objects import matrix

def DFS(x,y,matrix:matrix):  
  if x<0 or y<0 or x>=matrix.n or y >= matrix.m or matrix.visited[x][y]:
    return 0
  
  matrix.increaseSteps()

  matrix.setVisitedTrue(x,y)
  #Moverse a la derecha
  DFS(x = x+matrix.data[x][y], y=y, matrix = matrix)
  #Moverse a la izquierda
  DFS(x = x-matrix.data[x][y], y=y, matrix = matrix)
  #Moverse arriba
  DFS(x = x, y = y + matrix.data[x][y], matrix = matrix)
  #Moverse abajo
  DFS(x = x, y = y - matrix.data[x][y], matrix = matrix)

  matrix.setVisitedFalse(x,y)
  
  if matrix.data[x][y] == 0:
    return matrix.getSteps() + 1





#def uniformCost():
