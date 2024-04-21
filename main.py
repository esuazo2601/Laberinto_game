import pygame
from objects import matrix
from load_matrix import leer_archivo
from algorithms import DFS, uniformCost,getMinorSteps

#ToDo: Cambiar de puzzle con las flechas

# pygame setup
pygame.init()
width = 1020
height = 800
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

#DFS(x=puzzles[0].xstart,y=puzzles[0].ystart,matrix=puzzles[0])

print(puzzles[2].data)

#puzzles[0].flush()

#uniformCost(x=puzzles[0].xstart,y=puzzles[0].ystart,matrix=puzzles[0])

#print(puzzles[0].steps) 

steps = -1
current_mat = 0

while running:
    current_puzzle = puzzles[current_mat]
    # event manager
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_mat = (current_mat - 1) % len(puzzles)
            if event.key == pygame.K_RIGHT:
                current_mat = (current_mat + 1) % len(puzzles)
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                steps = getMinorSteps(puzzles[current_mat].xstart,puzzles[current_mat].ystart,puzzles[current_mat])
                if steps == -1 or steps == 0:
                    steps = "No hay solución"
                print(steps)
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill("white")
    #Contador de puzzle inferior
    mat_counter = smallfont.render(f'{current_mat + 1}/{cant_matrices}',True,(0,0,0))
    screen.blit(mat_counter,(width/2 - mat_counter.get_width() / 2,height - 60))
    #Contador de pasos de solucion

    step_counter = smallfont.render(f'Pasos para solución: {steps}',True,(0,0,0))
    screen.blit(step_counter,(width/2 - step_counter.get_width() / 2, height /2 - 350 ))

    #Para mostrar el puzzle actual
    current_puzzle.print(screen, (width / 2) - (current_puzzle.cell_size * current_puzzle.n)/2, height / 4)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)
pygame.quit() 