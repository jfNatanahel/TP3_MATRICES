m = int(input("Ingrese el número de filas: "))  # Número de filas
n = int(input("Ingrese el número de columnas: "))  # Número de columnas

# Crear una matriz (lista 2D) de dimensiones m x n
a = [[0 for k in range(n)] for k in range(m)]

# Llenar la matriz con valores proporcionados por el usuario
for i in range(m):
    for j in range(n):
        a[i][j] = int(input(f"Ingrese el valor para la posición ({i+1}, {j+1}): "))

# Imprimir la matriz original
print("\nMatriz Original:")
print(a)

# Ordenar cada fila de la matriz en orden ascendente
for i in range(m):
    c = 0
    v = [None] * n  # Crear un vector para almacenar temporalmente la fila
    for j in range(n):
        v[c] = a[i][j]
        c = c + 1

    # Ordenar el vector
    ordenar = sorted(v)

    # Actualizar la fila original con los valores ordenados
    c = 0
    for j in range(n):
        a[i][j] = ordenar[c]
        c = c + 1

# Imprimir la matriz ordenada por filas
print("\nMatriz Ordenada:")
for i in range(m):
    print()
    for j in range(n):
        print(a[i][j], "-", end="")
