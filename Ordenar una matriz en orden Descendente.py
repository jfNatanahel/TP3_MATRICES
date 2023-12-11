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

print("Matriz en orden ASCENDENTE")
#Ordenar en orden ascendente
matriz=[sorted(filas, reverse=True)for filas in matriz]
for filas in matriz:
    print("\t".join(map(str,filas)))

#reverse=True?
"""
El argumento reverse=True en la función sorted se utiliza para indicar que la ordenación se realice en orden descendente 
en lugar del orden ascendente predeterminado. Cuando reverse=True, la función sorted ordena los elementos del iterable en 
orden descendente.
"""