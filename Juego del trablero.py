"""
Se posee un tablero de 8 filas por 6 columnas, que tiene los numeros 2,4 y 6 en cada celda.
El jugador lanzara 5 dados, las cuales caeran en uno de los espacios del tablero, al final se deberan sumar todos los valores de los
espacios (celdas) donde cayeron los 5 dados.

Dependiendo de la suma de los valores de los espacios en las que cayeron las canicas el jugador gana premio.

Simular el juego del tablero:
    1) Carga la matriz y verificar que solo permita los valores 2,4 y 6. En caso contrario pedir de nuevo.
    2) Suponer que el orden de carga de los valores en la matriz ya se conoce.
    3) Simular el lanzamiento de los 5 dados.
    4) Mostrar la suma.
"""
filas = 8
columnas = 6
tablero = []

# Punto 1: Carga la matriz y verificar que solo permita los valores 2, 4 y 6.
for i in range(filas):
    fila = []
    for j in range(columnas):
        while True:
            numero = int(input(f"Ingresar un número (2, 4, 6) para la posición ({i+1},{j+1}): "))
            if numero in [2, 4, 6]:
                fila.append(numero)
                break
            else:
                print("El número debe ser 2, 4 o 6. VUELVA A INGRESAR EL VALOR.")

    tablero.append(fila)

# Punto 2: Suponer que el orden de carga de los valores en la matriz ya se conoce.
# Aquí simplemente imprimo el tablero. En el juego real, deberías lanzar los dados y calcular la suma.
print("Tablero:")
for fila in tablero:
    print(fila)

# Punto 3: Simular el lanzamiento de los 5 dados con entrada del usuario.
dados_lanzados = []
for _ in range(5):
    fila_dado = int(input("Ingrese la fila donde cayó el dado (1-8): ")) - 1
#-1?En este caso específico, cuando el usuario ingresa la fila donde cayó el
#dado en el rango de 1 a 8, se resta 1 para ajustar ese número al índice de Python.
    columna_dado = int(input("Ingrese la columna donde cayó el dado (1-6): ")) - 1

    if 0 <= fila_dado < filas and 0 <= columna_dado < columnas:
        resultado_dado = tablero[fila_dado][columna_dado]
        dados_lanzados.append(resultado_dado)
    else:
        print("Posición fuera de rango. Inténtelo de nuevo.")
        _ -= 1

# Punto 4: Mostrar la suma.
suma_lanzamiento = sum(dados_lanzados)
print("Resultado del lanzamiento de los dados:", suma_lanzamiento)
