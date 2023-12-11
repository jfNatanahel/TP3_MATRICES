import random

filas = 8
columnas = 6
tablero = []

# Punto 1: Carga la matriz y verificar que solo permita los valores 2, 4 y 6.
for i in range(filas):
    fila = []
    for j in range(columnas):
        numero = random.choice([2, 4, 6])
        fila.append(numero)

    tablero.append(fila)

# Punto 2: Suponer que el orden de carga de los valores en la matriz ya se conoce.
# Aquí simplemente imprimo el tablero. En el juego real, deberías lanzar los dados y calcular la suma.
print("Tablero:")
for fila in tablero:
    print(fila)

# Punto 3: Simular el lanzamiento de los 5 dados con números aleatorios.
dados_lanzados = []
for i in range(5):
    resultado_dado = random.choice([2, 4, 6])
    dados_lanzados.append(resultado_dado)


# Punto 4: Mostrar la suma.
suma_lanzamiento = sum(dados_lanzados)
print("Resultado del lanzamiento de los dados:", suma_lanzamiento)
