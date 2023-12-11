"""
Dada una matriz de MxN elementos numericos, calcular y mostrar la suma de todas las diagonales inferiores a la diagonal principal.
"""
# Ingresar el tamaño de las filas y columnas
filas = int(input("Ingresar el número de filas: "))
columnas = int(input("Ingresar el número de columnas: "))

# Crear la matriz
matriz = [[int(input(f"Ingrese el valor para la posición ({i+1},{j+1}):")) for j in range(columnas)] for i in range(filas)]

# Mostrar la matriz
print("\nMatriz ingresada:")
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end="\t")
    print()

# Calcular y mostrar la suma de todas las diagonales inferiores a la principal
if filas == columnas:
    sumas_diagonales = []
    for i in range(filas):
        suma_diagonal_i = 0
        for j in range(i):  # Iterar solo hasta la diagonal principal
            suma_diagonal_i += matriz[i][j]
        sumas_diagonales.append(suma_diagonal_i)

    # Mostrar cada suma individual
    for i, suma in enumerate(sumas_diagonales):
        print(f"La suma S{i+1} es:", suma)
    
    #Mostrar el resultado final
    suma_total = sum(sumas_diagonales)
    print("\nLa suma total de todas las diagonales inferiores a la principal es:", suma_total)
    
else:
    print("La matriz no es cuadrada, no tiene diagonal principal.")
