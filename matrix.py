import numpy as np
import pygame

class matrix:
    m = 0
    n = 0
    
    xstart = 0
    ystart = 0

    xend = 0
    yend = 0

    def __init__(self, matrix, dimensions):
        # Dimensiones de la matriz
        self.m = dimensions[0]
        self.n = dimensions[1]

        #Auxiliares de DFS
        self.visited_dfs = np.zeros((self.m,self.n),dtype=bool)
        self.current_path_dfs = []
        self.shortest_path_dfs = []
        self.shortest_path_length = float('inf')

        #Auxiliares UCOST
        self.steps_ucost = float('inf')
        self.path_ucost = []

        self.last_algorithm = None

        # Ajustar el tamaño de la celda según el número de columnas
        if self.n >= 20:
            self.cell_size = 32
        elif self.n >= 10:
            self.cell_size = 45
        else:
            self.cell_size = 80

        # Ajustar el tamaño de la fuente
        self.font_size = min(self.cell_size // 2, 35)

        # Posicion de inicio en x e y 
        self.xstart = dimensions[2]
        self.ystart = dimensions[3]
        
        # Posicion final en x e y
        self.xend = dimensions[4]
        self.yend = dimensions[5]
        
        # Matriz en sí
        self.data = np.array(matrix)

    def print(self, screen, posx, posy, show_dfs=False, show_ucost=False):
        for i in range(self.m):
            for j in range(self.n):
                # Calcular la posición de la celda en la ventana de Pygame
                x = posx + j * self.cell_size
                y = posy + i * self.cell_size
                
                # Obtener el valor de la celda en la matriz
                value = self.data[i][j]

                # Textos para los valores normales y para el valor de llegada
                font = pygame.font.SysFont('Corbel', self.font_size)
                index_font = pygame.font.SysFont('Corbel', int(self.font_size - self.font_size / 2.5))
                final = font.render('G', False, (50, 205, 50))
                text = font.render(str(value), True, (255, 255, 255))
                
                # Si hay un 0, es el final y se muestra G, si no se muestra el valor de la celda
                if value == 0:
                    pygame.draw.rect(screen, (0, 0, 0), (x, y, self.cell_size, self.cell_size))
                    screen.blit(final, (x + self.cell_size // 2 - final.get_width() // 2, y + self.cell_size // 2 - final.get_height() // 2))
                    
                    if show_dfs and (i, j) in self.shortest_path_dfs:
                        pygame.draw.rect(screen, (0, 0, 255), (x, y, self.cell_size, self.cell_size), 3)
                        index_text = index_font.render(str(self.shortest_path_dfs.index((i, j))), True, (255, 255, 255))
                        screen.blit(index_text, (x + self.cell_size - index_text.get_width() - 5, y + self.cell_size - index_text.get_height()))
    
                    if show_ucost and (i, j) in self.path_ucost:
                        pygame.draw.rect(screen, (255, 0, 0), (x, y, self.cell_size, self.cell_size), 3)
                        # Mostrar el índice abajo a la derecha
                        index_text = index_font.render(str(self.path_ucost.index((i, j))), True, (255, 255, 255))
                        screen.blit(index_text, (x + self.cell_size - index_text.get_width() - 5, y + self.cell_size - index_text.get_height()))

                elif value != 0:
                    pygame.draw.rect(screen, (0, 0, 0), (x, y, self.cell_size, self.cell_size))       
                    screen.blit(text, (x + self.cell_size // 2 - text.get_width() // 2, y + self.cell_size // 2 - text.get_height() // 2))
                    # Destacar la celda de inicio con un círculo blanco
                    if i == self.xstart and j == self.ystart:
                        pygame.draw.circle(screen, (30, 144, 255), (int(x + self.cell_size / 2), int(y + self.cell_size / 2)), int(self.cell_size / 2.2), 3)
                    
                    # Resaltar las celdas de la solución UCOST y mostrar el índice
                    if show_dfs and (i, j) in self.shortest_path_dfs:
                        pygame.draw.rect(screen, (0, 0, 255), (x, y, self.cell_size, self.cell_size), 3)
                        # Mostrar el índice abajo a la derecha
                        index_text = index_font.render(str(self.shortest_path_dfs.index((i, j))), True, (255, 255, 255))
                        screen.blit(index_text, (x + self.cell_size - index_text.get_width()- 5, y + self.cell_size - index_text.get_height()))
                    # Resaltar las celdas de la solución DFS y mostrar el índice
                    if show_ucost and (i, j) in self.path_ucost:
                        pygame.draw.rect(screen, (255, 0, 0), (x, y, self.cell_size, self.cell_size), 3)
                        # Mostrar el índice abajo a la derecha
                        index_text = index_font.render(str(self.path_ucost.index((i, j))), True, (255, 255, 255))
                        screen.blit(index_text, (x + self.cell_size - index_text.get_width() - 5, y + self.cell_size - index_text.get_height()))

