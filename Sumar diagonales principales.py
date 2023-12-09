
filas=int(input("Ingresar el tamaño de las filas: "))
columnas=int(input("Ingresar el tamaño de las columnas: "))

#Crear la matriz
matriz=[[int(input(f"Ingrese el valor para la posicion ({i+1},{j+1}):"))for i in range(filas)]for j in range(columnas)]

#Mostrar la matriz para ver como quedan con los valores ingresados por el usuario.
print("Matriz ingresada")
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end="\t")
    print()

#Sumar las diagonales
suma_diagonales=0
if filas == columnas:
    for i in range(filas):
        suma_diagonales=suma_diagonales+matriz[i][i]
    print("La suma de la diagonal principal es: ",suma_diagonales)
else:
    print("La matriz no es cuadrada, no tiene diagonal principal")
