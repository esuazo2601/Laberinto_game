import pygame
from objects import matrix
from load_matrix import leer_archivo

#ToDo: Cambiar de puzzle con las flechas

# pygame setup
pygame.init()
width = 800
height = 640
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
smallfont = pygame.font.SysFont('Corbel',35) 
#

#PUZZLES SETUP
matrices, dimensiones = leer_archivo("input.txt")
puzzles:matrix = []
cant_matrices = len(matrices)

for i in range(cant_matrices):
    mat = matrix(matrices[i],dimensiones[i])
    puzzles.append(mat)

print(puzzles[0].data)
#

current_mat = 0
mat_counter = smallfont.render(f'{current_mat + 1}/{cant_matrices}',True,(0,0,0))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    screen.blit(mat_counter,(width/2,height - 60))
    
    current_puzzle = puzzles[current_mat]
    current_puzzle.print(screen, (width / 2) - (current_puzzle.cell_size * current_puzzle.n)/2, height / 4)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit() 
