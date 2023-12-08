#Sopa de letras - programa en python solo para buscar una palabra en forma horizontal
#Crear la matriz de la sopa de letra
filas=int(input("Ingresar el tamaño de las filas: "))
columnas=int(input("Ingresar el tamaño de las columnas: "))
sopa_de_letras=[]
for i in range(filas):
    fila=[]
    for j in range(columnas):
        elemento=str(input(f"Ingresar los elementos ({i+1},{j+1}): "))
        fila.append(elemento)
    sopa_de_letras.append(fila)

#Crear la matriz donde estar los elementos encontrados en la sopa de letra
palabras_encontradas=[]
for i in range(filas):
    palabras_encontradas.append([None]*columnas)
        

#Mostrar la sopa de letra
for i in range(filas):
    for j in range(columnas):
        print(sopa_de_letras[i][j], end="\t")
    print()

palabra_buscar=int(input("Ingresar la palabra a buscar en la sopa de letra: "))

for fila in sopa_de_letras:
    derecha_izquierda="".join(reversed(fila))

#Buscar la palabra de derecha a izquierda
    if palabra_buscar in derecha_izquierda:
        palabras_encontradas.append(derecha_izquierda)

#Buscar la palabra de izquierda a derecha
    izquierda_derecha="".join(fila)
    if palabra_buscar in izquierda_derecha:
        palabras_encontradas.append(izquierda_derecha)

#Mostrar las palabras encontradas
for i in range(filas):
    for j in range(columnas):
        print(palabras_encontradas[i][j], end="\t")
    print()