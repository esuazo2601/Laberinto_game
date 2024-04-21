from objects import matrix
import heapq

def isInvalidMove(x,y, matrix:matrix):
    return x < 0 or y < 0 or x >= matrix.n or y >= matrix.m or matrix.visited[x][y]

def DFS(x, y, matrix:matrix):
    if isInvalidMove(x,y,matrix):
        return
    
    #print(f"{(x, y)}" ":" f"{matrix.data[x][y]}" )
    matrix.steps += 1

    if x == matrix.xend and y == matrix.yend:
        return

    matrix.visited[x][y] = True
    #Moverse abajo
    DFS(x = x, y = y - matrix.data[x][y], matrix = matrix)
    #Moverse a la derecha
    DFS(x = x + matrix.data[x][y],y = y, matrix = matrix)
    #Moverse a la izquierda
    DFS(x = x - matrix.data[x][y],y = y, matrix = matrix)
    #Moverse arriba
    DFS(x = x, y = y + matrix.data[x][y], matrix = matrix)

    #matrix.visited[x][y] = False

def uniformCost(x,y,matrix:matrix):
    pq = [(0,matrix.xstart, matrix.ystart)]
    while pq:
        cost, x ,y = heapq.heappop(pq)
        
        if x == matrix.xend and y == matrix.yend:
            matrix.steps = cost
            return
        
        if matrix.visited[x][y]:
            continue
        
        matrix.visited[x][y] = True
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx,dy in moves:
            new_x,new_y = x + dx * matrix.data[x][y], y + dy * matrix.data[x][y]
            if not isInvalidMove(new_x,new_y,matrix):
                heapq.heappush(pq,(cost+1,new_x,new_y))
    return -1

def getMinorSteps(x, y, matrix:matrix):
    steps_dfs = 0
    steps_ucost = 0
    
    DFS(x,y,matrix)
    steps_dfs = matrix.steps

    matrix.flush()

    uniformCost(x,y,matrix)
    steps_ucost = matrix.steps
    
    return min(steps_dfs,steps_ucost)

