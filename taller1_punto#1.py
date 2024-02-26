#1. Realice un programa que sume, reste, multiplique (producto punto y producto cruz) y divida dos vectores previamente inicializados:
import numpy as np
# Inicialización de dos vectores
vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
# Suma
suma = vector_a + vector_b
# Resta
resta = vector_a - vector_b
# Producto punto
producto_punto = np.dot(vector_a, vector_b)
# Producto cruz
producto_cruz = np.cross(vector_a, vector_b)
# División elemento a elemento
# Para evitar la división por cero, se añade un pequeño valor a vector_b
division = vector_a / (vector_b + 1e-9)
print("Suma:", suma)
print("Resta:", resta)
print("Producto punto:", producto_punto)
print("Producto cruz:", producto_cruz)
print("División:", division)
