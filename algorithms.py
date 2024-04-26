from matrix import matrix
import heapq
import numpy as np

def isInvalidMove(x, y, matrix):
    if x < 0 or x >= len(matrix.data) or y < 0 or y >= len(matrix.data[0]) or matrix.visited_dfs[x][y]:
        return True
    return False

def DFS(x, y, matrix:matrix, steps):
    #Si el movimiento no es valido, no seguimos por ahi
    if isInvalidMove(x,y,matrix):
        return
    
    #De lo contrario agregamos la posicion actual en el camino actual
    matrix.current_path_dfs.append((x,y))

    #Si llegamos al final
    if x == matrix.xend and y == matrix.yend:
        if steps < matrix.shortest_path_length: #y la cantidad de pasos es menor que la del camino mas corto encontrado
            matrix.shortest_path_length = steps #se reemplaza
            matrix.shortest_path = list(matrix.current_path_dfs) 
        matrix.current_path_dfs.pop()
        return
            
    matrix.visited_dfs[x][y] = True

    #Moverse abajo
    DFS(x = x, y = y - matrix.data[x][y], matrix = matrix, steps = steps + 1)
    #Moverse a la derecha
    DFS(x = x + matrix.data[x][y],y = y, matrix = matrix, steps = steps + 1)
    #Moverse a la izquierda
    DFS(x = x - matrix.data[x][y],y = y, matrix = matrix, steps = steps + 1)
    #Moverse arriba
    DFS(x = x, y = y + matrix.data[x][y], matrix = matrix, steps = steps + 1)

    matrix.visited_dfs[x][y] = False
    matrix.current_path_dfs.pop()


def uniformCost(x,y,matrix:matrix):
    #Priority queue a usar 
    pq = [(0,matrix.xstart, matrix.ystart)]

    while pq:
        cost, x ,y = heapq.heappop(pq)
        #print(x,y)
        
        #Si llegamos al final retornamos los pasos
        if x == matrix.xend and y == matrix.yend:
            matrix.steps = cost
            return
        
        if matrix.visited[x][y]:
            continue
        
        matrix.visited[x][y] = True
        #Vector de posibles movimientos
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        #Moverse si el movimiento es válido
        for dx,dy in moves:
            new_x,new_y = x + dx * matrix.data[x][y], y + dy * matrix.data[x][y]
            if not isInvalidMove(new_x,new_y,matrix):
                heapq.heappush(pq,(cost+1,new_x,new_y))
    #Retornaremos -1 si no se encuentra solución
    return -1


#Retorna los pasos del algoritmo que sea mas eficiente
def getMinorSteps(x, y, matrix:matrix):
    #steps_dfs = 0
    #steps_ucost = 0
    
    DFS(x,y,matrix,0)
    print("camino mas corto:", matrix.shortest_path_length)
    

    #matrix.flush()

    #uniformCost(x,y,matrix)
    #steps_ucost = matrix.steps
    #print(f"UCOST: {steps_ucost}")
    return matrix.shortest_path_length
    #return min(steps_dfs,steps_ucost)

