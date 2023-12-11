filas=int(input("Ingresar el numero de filas: "))
columnas=int(input("Ingresar el numero de columnas: "))
matriz=[]

#Iterar a traves de las filas
for i in range(filas):
    fila=[] #Iniciar una lista vacia para cada fila
    #Iterar a travez de las columnas en cada fila
    for j in range(columnas):
        elemento=int(input(f"Ingrese el elemento en la posicion ({i+1},{j+1}): "))
        fila.append(elemento) #Agregar el elemento a la fila actual
    matriz.append(fila) #Agregar la fila a la matriz

#1)Mostrar la matriz:
for fila in matriz: #Iterar a traves de cada fila en la matriz
    print(fila) #Imprime la fila.


#2)Mostrar la matriz:
print("Matriz ingresada:")
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end="\t") 
    print()#Salto de linea
#end="\t" se utiliza para especificar que después de imprimir cada elemento de la fila, se agregará un tabulador