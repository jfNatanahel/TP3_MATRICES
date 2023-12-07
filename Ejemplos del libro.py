#Arreglo del 0 al 9 usando numpy
import numpy as np 
"""a=numpy.arange(10)
print(a)"""

#Crear un arreglo multidimensional 2x2 con tipo de dato int32
"""A=np.array([[1,2],[2,4]],np.int32)
print(A)
print(A.shape) #Forma del arreglo
print(A.size) #El tamaño"""

#Ejemplo 14.3: Cambiando la forma de un arreglo utilizando la funcion Reshape.
"""a=np.arange(10)
print(a) #Vector (Arreglo) dimension 10
print(a.reshape(2,5)) #Matriz de 10 elementos = al vector¡¡¡¡¡¡¡¡¡¡
print(max(a))"""

#Ejemplo 14.6: Realizar busquedas de datos usando los indices de la matrices.
a=np.random.rand(3,3)
print(a)
print("Mostramos la 1ra y 2da columna", a[:,0:2])