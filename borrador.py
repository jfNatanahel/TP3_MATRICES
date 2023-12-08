# Sopa de letras - programa en python solo para buscar una palabra en forma horizontal
# Crear la matriz de la sopa de letra
filas = int(input("Ingresar el tamaño de las filas: "))
columnas = int(input("Ingresar el tamaño de las columnas: "))
sopa_de_letras = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        elemento = str(input(f"Ingresar los elementos ({i+1},{j+1}): "))
        fila.append(elemento)
    sopa_de_letras.append(fila)

# Crear la matriz donde estar los elementos encontrados en la sopa de letra
palabras_encontradas = [["" for _ in range(columnas)] for _ in range(filas)]

# Mostrar la sopa de letra
for i in range(filas):
    for j in range(columnas):
        print(sopa_de_letras[i][j], end="\t")
    print()

palabra_buscar = input("Ingresar la palabra a buscar en la sopa de letra: ")

# Buscar la palabra en cada fila
for i in range(filas):
    fila_str = ''.join(sopa_de_letras[i])
    derecha_izquierda = ''.join(reversed(fila_str))

    # Buscar la palabra de derecha a izquierda
    if palabra_buscar in derecha_izquierda:
        palabras_encontradas[i] = derecha_izquierda

    # Buscar la palabra de izquierda a derecha
    if palabra_buscar in fila_str:
        palabras_encontradas[i] = fila_str

# Mostrar las palabras encontradas
print("Palabras encontradas:")
for i in range(filas):
    print(palabras_encontradas[i])
