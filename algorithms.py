from matrix import matrix
from queue import PriorityQueue

def isInvalidMove(x, y, matrix):
    if x < 0 or x >= len(matrix.data) or y < 0 or y >= len(matrix.data[0]):
        return True
    return False

def construct_path(path, xend, yend):
    result = []
    current = (xend, yend)
    while current:
        result.append(current)
        current = path[current]
    result.reverse()
    return result


def DFS(x, y, matrix:matrix, steps):
    #Si el movimiento no es valido, no seguimos por ahi
    if isInvalidMove (x,y,matrix) or matrix.visited_dfs[x][y]:
        return
    
    #De lo contrario agregamos la posicion actual en el camino actual
    matrix.current_path_dfs.append((x,y))

    #Si llegamos al final
    if x == matrix.xend and y == matrix.yend:
        if steps < matrix.shortest_path_length: #y la cantidad de pasos es menor que la del camino mas corto encontrado
            matrix.shortest_path_length = steps #se reemplaza
            matrix.shortest_path_dfs = list(matrix.current_path_dfs) 
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


def uniformCost(x, y, matrix):
    # Movimientos
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Priority queue a usar
    pq = PriorityQueue()
    
    # Diccionario de costos y camino
    costs = {(x, y): 0}
    path = {(x, y): None}

    # Entra el primer valor, con costo 0
    pq.put((0, (x, y)))
    #Iteramos mientras no se vacie la pq
    while not pq.empty():
        #Sacamos el primer valor
        cost, (x, y) = pq.get()
        #Si estamos en el final retornamos el costo y construimos el camino mas corto encontrado
        if x == matrix.xend and y == matrix.yend:
            return cost, construct_path(path, matrix.xend, matrix.yend)
        
        no_valid_move = True
        

        for dx, dy in moves:
            # Ubicamos los nuevos x e y
            new_x, new_y = x + dx * matrix.data[x][y], y + dy * matrix.data[x][y]
            #Si son validos
            if not isInvalidMove(new_x, new_y, matrix):
                #El nuevo costo sera el anterior + 1
                new_cost = cost + 1
                #Si el nuevo destino no se encunetra en los costos o el costo es menor que el que habia
                if (new_x, new_y) not in costs or new_cost < costs[(new_x, new_y)]:
                    costs[(new_x, new_y)] = new_cost #Se agrega al diccionario de costos
                    pq.put((new_cost, (new_x, new_y))) #se pushea la nueva posicion a la pq
                    path[(new_x, new_y)] = (x, y) #Camino: Donde estoy ahora = donde estaba
                    no_valid_move = False
        
        if no_valid_move:
            continue

    # Si no se encuentra un camino válido, se devuelve -1 y camino vacio
    return -1, []
