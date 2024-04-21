import heapq

def is_valid_move(grid, visited, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and not visited[x][y]

def uniform_cost_search(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    start_x, start_y = 0, 0
    dest_x, dest_y = 1,3
    
    # Mantener una cola de prioridad de nodos a explorar
    pq = [(0, start_x, start_y)]  # (costo acumulado, x, y)
    
    while pq:
        cost, x, y = heapq.heappop(pq)
        if x == dest_x and y == dest_y:
            return cost
        
        if visited[x][y]:
            continue
        
        visited[x][y] = True
        print(f"{(x,y)}")

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in moves:
            new_x, new_y = x + dx * grid[x][y], y + dy * grid[x][y]
            if is_valid_move(grid, visited, new_x, new_y):
                heapq.heappush(pq, (cost + 1, new_x, new_y))
    
    # Si no se encuentra un camino válido
    return -1

# Ejemplo de uso
grid = [
    [3, 4, 1, 3, 1],
    [3, 3, 3, 0, 2],
    [3, 1, 2, 2, 3],
    [4, 2, 3, 3, 3],
    [4, 1, 4, 3, 2]
]

print("La longitud del camino más corto es:", uniform_cost_search(grid))
