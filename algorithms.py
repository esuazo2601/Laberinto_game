from objects import matrix

def DFS(x, y, matrix):
    if x < 0 or y < 0 or x >= matrix.n or y >= matrix.m or matrix.visited[x][y]:
        return 0
    
    if matrix.data[x][y] == 0:
        return matrix.getSteps() + 1

    matrix.increaseSteps()
    matrix.setVisitedTrue(x, y)

    print(f"{x,y}\n")

    # Moverse a la derecha
    result = DFS(x + matrix.data[x][y], y, matrix)
    if result != 0:
        return result

    # Moverse a la izquierda
    result = DFS(x - matrix.data[x][y], y, matrix)
    if result != 0:
        return result

    # Moverse arriba
    result = DFS(x, y + matrix.data[x][y], matrix)
    if result != 0:
        return result

    # Moverse abajo
    result = DFS(x, y - matrix.data[x][y], matrix)
    if result != 0:
        return result

    matrix.setVisitedFalse(x, y)

#def uniformCost():
