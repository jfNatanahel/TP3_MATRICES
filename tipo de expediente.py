"""
Dada una matriz A de MxN que contiene N° de Expediente, donde los 3 
primeros caracerteres identifican el tipo de expediente.
ADM (Administrativo) y JUD (judiciales)

a)Se desea identificar los expedientes Administrativos e insertarlos 
posteriormente en una nueva matriz B. Se debe respetar la posicion
y dejar en blanco el espacio de Matriz B de no corresponder.

b)Se desea contabilziar y mostrar la cantidad total de expedientes ADM y JUD.

c)Mostrar la cantidad total de Expedientes ADM y JUD.

"""
filas=int(input("Ingresar el tamaño de las filas de la matriz: "))
columnas=int(input("Ingresar el tamaño de las columnas de la matriz: "))

#Crear la matriz donde estaran los expedientes ADM y JUD
contador_administrativos=0
contador_judiciales=0
expedientes=[]
for i in range(filas):
    fila=[]
    for j in range(columnas):
        elemento=str(input(f"Ingresar el valor en la posicion({i+1},{j+1}): "))
        #c)Contar la cantidad de expediente
        if elemento[:3]=="ADM":
            contador_administrativos+=1
        else:
            contador_judiciales+=1
        fila.append(elemento)
    expedientes.append(fila)

#a)Identificar los expedientes Administrativos y cargarlos a una matriz B.
#Crear una matriz B vacia
B=[[0 for j in range(columnas)]for i in range(filas)]

#Reccorer la matriz A
for i in range(filas):
    for j in range(columnas):
        letra=expedientes[i][j]
        if letra[:3]=="ADM":
            B[i][j]=letra
#Mostrar la matriz B
print("Matriz B")
for i in range(filas):
    for j in range(columnas):
        print(B[i][j], end="\t")
    print()
print("C:cantidad total de expedientes")
print("Administrativos:",contador_administrativos)
print("Judiciales:",contador_judiciales)
