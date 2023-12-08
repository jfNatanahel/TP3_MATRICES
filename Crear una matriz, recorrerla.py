m = int(input("Ingrese el número de filas: "))
n = int(input("Ingrese el número de columnas: "))

# Crear una lista 2D y llenarla con la entrada del usuario
a = [[0 for i in range(n)] for k in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = int(input(f"Ingrese el elemento en la posición ({i+1}, {j+1}): "))

# Imprimir "Muestra 1" seguido de toda la lista 2D
print("Muestra 1")
print(a)

# Imprimir "Muestra 2" e iterar a través de la lista 2D para imprimir cada elemento con un separador "-"
print("Muestra 2")
for i in range(m):
    print()
    for j in range(n):
        print(a[i][j], end="\t")
