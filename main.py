import pygame
from objects import matrix
from load_matrix import leer_archivo

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 640))
clock = pygame.time.Clock()
running = True


matrices, dimensiones = leer_archivo("input.txt")
puzzles:matrix = []
cant_matrices = len(matrices)

for i in range(cant_matrices):
    mat = matrix(matrices[i],dimensiones[i])
    puzzles.append(mat)

print(puzzles)


""" 
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit() 

"""