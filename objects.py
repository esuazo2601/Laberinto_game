import numpy as np
import pygame

class matrix:
    m = 0
    n = 0
    
    xstart = 0
    ystart = 0

    xend = 0
    yend = 0

    cell_size = 80

    def __init__(self, matrix, dimensions):
        # Dimensiones de la matriz
        self.m = dimensions[0]
        self.n = dimensions[1]

        # Posicion de inicio en x e y 
        self.xstart = dimensions[2]
        self.ystart = dimensions[3]
        
        # Posicion final en x e y
        self.xend = dimensions[4]
        self.yend = dimensions[5]
        
        # Matriz en sí
        self.data = np.array(matrix)

    def print(self, screen, posx, posy):
        for i in range(self.m):
            for j in range(self.n):
                # Calcular la posición de la celda en la ventana de Pygame
                x = posx + j * self.cell_size
                y = posy + i * self.cell_size
                
                # Obtener el valor de la celda en la matriz
                value = self.data[i][j]

                # Textos para los valores normales y para el valor de llegada
                font = pygame.font.SysFont('Corbel', 35)
                final = font.render('G', False, (255, 255, 255))
                text = font.render(str(value), True, (255, 255, 255))
                
                # Si hay un 0, es el final y se muestra G, si no se muestra el valor de la celda
                if value == 0:
                    pygame.draw.rect(screen, (0, 0, 0), (x, y, self.cell_size, self.cell_size))
                    screen.blit(final, (x + self.cell_size // 2 - final.get_width() // 2, y + self.cell_size // 2 - final.get_height() // 2))
                elif value != 0:
                    pygame.draw.rect(screen, (0, 0, 0), (x, y, self.cell_size, self.cell_size))
                    screen.blit(text, (x + self.cell_size // 2 - text.get_width() // 2, y + self.cell_size // 2 - text.get_height() // 2))
                    # Destacar la celda de inicio con un círculo blanco sin rellenar
                    if i == self.xstart and j == self.ystart:
                        pygame.draw.circle(surface=screen, color=(255, 255, 255), center=(int(x + self.cell_size / 2), int(y + self.cell_size / 2)), radius = int(self.cell_size / 2.2), width=3)




