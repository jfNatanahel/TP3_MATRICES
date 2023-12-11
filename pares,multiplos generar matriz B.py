"""
Condiciones para generar la matriz B:
1.Encontrar de matriz A los numeros pares y multiplos de X
2.Generar y mostrar la matriz resultante B.
3.Los numeros de la condicion (1) deben respetar el mismo lugar en la matriz B. 
"""


filas=int(input("Ingresar el tamaño de las filas: "))
columnas=int(input("Ingresar el tamaño de las columnas: "))

#Crear la matriz A
A=[[int(input(f"Ingresar los valores en la posicion ({i+1},{j+1}): "))for j in range(columnas)]for i in range(filas)]

#Mostrar el vector A
for i in range(filas):
    for j in range(columnas):
        print(A[i][j], end="\t")
    print()

#Crear la matriz B. Para pasar los pares que sean multiplos de x
B=[[0 for k in range(columnas)]for k in range(filas)]

x=int(input("Ingresar numero para buscar en la matriz A los pares que son multiplos de x: "))

#Buscar los pares, multiplos de x
for i in range(filas):
    for j in range(columnas):
        numero=A[i][j]
        if numero%2==0 and numero%x==0:
            B[i][j]=numero #EL NUMERO VAYA A LA POSICION CORRECTA!!!

#Mostrar el vector B
for i in range(filas):
    for j in range(columnas):
        print(B[i][j], end="\t")
    print()


