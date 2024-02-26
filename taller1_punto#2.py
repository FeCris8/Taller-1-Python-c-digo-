#2. Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos matrices previamente inicializadas:
import numpy as np
# Inicialización de dos matrices
matriz_a = np.array([[1, 2], [3, 4]])
matriz_b = np.array([[5, 6], [7, 8]])
# Suma
suma = np.add(matriz_a, matriz_b)
# Resta
resta = np.subtract(matriz_a, matriz_b)
# Multiplicación elemento a elemento
multiplicacion_elemento = np.multiply(matriz_a, matriz_b)
# Producto punto
producto_punto = np.dot(matriz_a, matriz_b)
# División elemento a elemento
# Para evitar la división por cero, se añade un pequeño valor a matriz_b
division = np.divide(matriz_a, matriz_b + 1e-9)
print("Suma:\n", suma)
print("Resta:\n", resta)
print("Multiplicación elemento a elemento:\n", multiplicacion_elemento)
print("Producto punto:\n", producto_punto)
print("División:\n", division)
"""realizar las operaciones básicas entre matrices. Tener en cuenta que el producto punto entre dos matrices solo es posible si el número de columnas de la primera 
#matriz es igual al número de filas de la segunda matriz. Asegúrse de que las matrices que inicialice cumplan con esta condición para que el producto punto funcione correctamente.
#Además, la división de matrices no es una operación estándar y aquí se muestra la división elemento a elemento"""