import pygame
from matrix import matrix
from load_matrix import leer_archivo
from algorithms import DFS, uniformCost

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
matrices, dimensiones = leer_archivo("input_1.txt")
puzzles:matrix = []
cant_matrices = len(matrices)

for i in range(cant_matrices):
    mat = matrix(matrices[i],dimensiones[i])
    puzzles.append(mat)

steps = 'Pulse d o f'
current_mat = 0
#Los laberintos quedan en la lista puzzles

#Mainloop
while running:
    current_puzzle: matrix = puzzles[current_mat]
    path_ucost = []
    # eventos
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_mat = (current_mat - 1) % len(puzzles)
            if event.key == pygame.K_RIGHT:
                current_mat = (current_mat + 1) % len(puzzles)
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_d:
                # Ejecutar DFS
                DFS(current_puzzle.xstart, current_puzzle.ystart, current_puzzle, 0)
                print("DFS: ", current_puzzle.shortest_path_dfs)

                steps = current_puzzle.shortest_path_length
                current_puzzle.last_algorithm = 'DFS'
            if event.key == pygame.K_f:
                # Ejecutar uniformCost
                steps, path_ucost = uniformCost(current_puzzle.xstart, current_puzzle.ystart, current_puzzle)
                print("UCOST: ",path_ucost)
                current_puzzle.steps_ucost = steps
                current_puzzle.path_ucost = path_ucost
                current_puzzle.last_algorithm = 'UCOST'

        if event.type == pygame.QUIT:
            running = False
        
    screen.fill("white")
    
    # Contador de puzzle inferior
    mat_counter = smallfont.render(f'{current_mat + 1}/{cant_matrices}', True, (0, 0, 0))
    screen.blit(mat_counter, (width/2 - mat_counter.get_width() / 2, height - 60))
    
    # Contador de pasos de solucion
    if steps == -1 or steps == 0 or steps == float('inf'):
        steps = 'NO HAY SOLUCIÓN'

    step_counter = smallfont.render(f'Pasos para solución: {steps}', True, (0, 0, 0))
    screen.blit(step_counter, (width/2 - step_counter.get_width() / 2, height / 2 - 350))

    # Para mostrar el puzzle actual
    current_puzzle.print(screen, (width / 2) - (current_puzzle.cell_size * current_puzzle.n)/2, height / 4, show_dfs=current_puzzle.last_algorithm == 'DFS', show_ucost=current_puzzle.last_algorithm == 'UCOST')

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)
pygame.quit()

