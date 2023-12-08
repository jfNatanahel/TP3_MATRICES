filas=int(input("Ingresar el tamaño de las filas: "))
columnas=int(input("Ingresar el tamaño de las columnas: "))
matriz=[[int(input(f"Ingresar el valor en la posicion ({i+1},{j+1}): "))for j in range(columnas)]for i in range(filas)]

#Mostrar la matriz
print("Matriz ingresada")
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end="\t")
    print()
#Compresion de listas:
"""sumas_columnas=[sum(matriz[i][j]for i in range(filas))for j in range(columnas)]
print("La suma de las columnas")"""

#Ciclo anidado:
sumas_columnas=[]
for j in range(columnas):
    suma=0
    for i in range(filas):
        suma=suma+matriz[i][j]
    sumas_columnas.append(suma)

# Mostrar las sumas de cada columna
print("\nSuma de cada columna:")
for j, suma in enumerate(sumas_columnas):
    print(f"Columna {j + 1}: {suma}")



    