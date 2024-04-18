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
