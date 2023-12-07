filas = int(input("Ingresar el número de filas: "))
columnas = int(input("Ingresar el número de columnas: "))

# Crear la matriz utilizando comprensión de listas
matriz = [[int(input(f"Ingrese el elemento en la posición ({i+1},{j+1}): ")) for j in range(columnas)] for i in range(filas)]

# Mostrar la matriz
print("Matriz ingresada:")
for fila in matriz:
    print(fila)
