#5.Realice en funciones las rotaciones en X, Y y Z, donde se tenga un parámetro de entrada (ángulo) y un parámetro de salida (matriz).
import numpy as np

def rotacion_x(angulo):
    """
    Calcula la matriz de rotación en el eje X.
    :param angulo: Ángulo en radianes.
    :return: Matriz de rotación en el eje X.
    """
    return np.array([[1, 0, 0],
                     [0, np.cos(angulo), -np.sin(angulo)],
                     [0, np.sin(angulo), np.cos(angulo)]])

def rotacion_y(angulo):
    """
    Calcula la matriz de rotación en el eje Y.
    :param angulo: Ángulo en radianes.
    :return: Matriz de rotación en el eje Y.
    """
    return np.array([[np.cos(angulo), 0, np.sin(angulo)],
                     [0, 1, 0],
                     [-np.sin(angulo), 0, np.cos(angulo)]])

def rotacion_z(angulo):
    """
    Calcula la matriz de rotación en el eje Z.
    :param angulo: Ángulo en radianes.
    :return: Matriz de rotación en el eje Z.
    """
    return np.array([[np.cos(angulo), -np.sin(angulo), 0],
                     [np.sin(angulo), np.cos(angulo), 0],
                     [0, 0, 1]])

# Ejemplo de uso
angulo_en_radianes = np.pi / 4  # Ángulo de 45 grados
matriz_rotacion_x = rotacion_x(angulo_en_radianes)
matriz_rotacion_y = rotacion_y(angulo_en_radianes)
matriz_rotacion_z = rotacion_z(angulo_en_radianes)

print("Matriz de rotación en el eje X:")
print(matriz_rotacion_x)

print("\nMatriz de rotación en el eje Y:")
print(matriz_rotacion_y)

print("\nMatriz de rotación en el eje Z:")
print(matriz_rotacion_z)

"""En este código, las funciones rotacion_x, rotacion_y y rotacion_z calculan las matrices de rotación en los ejes X, Y y Z, respectivamente. 
Puedes ajustar el ángulo según tus necesidades y obtener las matrices de rotación correspondientes"""