# Función para leer todas las matrices del archivo
def leer_archivo(nombre_archivo):
    matrices = []
    dimensiones = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            mat_dim = list(map(int, linea.split()))
            dimensiones.append(mat_dim)
            filas, columnas = mat_dim[:2]
            matriz = []
            for _ in range(filas):
                fila = list(map(int, archivo.readline().split()))
                matriz.append(fila)
            matrices.append(matriz)
    return matrices,dimensiones
""" 
# Llamar a la función y obtener todas las matrices
nombre_archivo = "input.txt"  # Reemplaza "archivo.txt" con el nombre de tu archivo
matrices, dimensiones = leer_archivo(nombre_archivo)

#print(f"{dimensiones}\n")
# Imprimir todas las matrices
for i, matriz in enumerate(matrices):
    print(f"Matriz {i+1}:")
    for fila in matriz:
        print(fila)
    print()
 """