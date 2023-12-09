filas = int(input("Ingresar el tamaño de las filas: "))
columnas = int(input("Ingresar el tamaño de las columnas: "))

# Crear la matriz A
A = [[int(input(f"Ingresar el elemento en la posicion ({i+1},{j+1}): ")) for j in range(columnas)] for i in range(filas)]

# Mostrar la matriz A
for i in range(filas):
    for j in range(columnas):
        print(A[i][j], end="\t")
    print()

# Creación del vector donde estarán los números impares con sus divisores
vector = []

# Encontrar los impares y sus divisores
for i in range(filas):
    for j in range(columnas):
        numero = A[i][j]
        if numero % 2 != 0:
            vector.append(numero)
            divisores = []
            for divisor in range(2, numero//2 + 1):
                if numero % divisor == 0 and divisor != numero and divisor != 1:
                    divisores.append(divisor)
            if len(divisores) == 0:
                vector.append(0)
            else:
                vector.extend(divisores)

# Mostrar el vector
print("Vector:")
print(vector)
