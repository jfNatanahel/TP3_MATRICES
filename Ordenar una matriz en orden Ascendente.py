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
matriz=[sorted(filas)for filas in matriz]
for filas in matriz:
    print("\t".join(map(str,filas)))







#Funciones utilizadas
"""
JOIN?? es un método de cadena que se utiliza para concatenar (unir) una secuencia de elementos en una sola cadena.
#Sintaxis: separador.join(iterable)

map??La función map se utiliza para aplicar una función a cada elemento de un iterable y devolver un nuevo iterable
con los resultados. Sintaxis= map(func, iterable)


"""
