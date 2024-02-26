#4. Consulte y elabore un sistema coordenado X, Y y Z donde se dibuje un vector con coordenadas ingresadas por el usuario.

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Solicitar al usuario que ingrese las coordenadas del vector
x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))
# Crear una figura y un sistema de coordenadas 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Dibujar el vector
ax.quiver(0, 0, 0, x, y, z)
# Establecer los límites de los ejes
ax.set_xlim([0, max(x, 1)])
ax.set_ylim([0, max(y, 1)])
ax.set_zlim([0, max(z, 1)])
# Etiquetas de los ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
# Mostrar el gráfico
plt.show()

"""crea un gráfico 3D y dibuja un vector desde el origen hasta el punto con las coordenadas ingresadas por el usuario.
El método quiver se utiliza para dibujar el vector en el espacio 3D, y los métodos set_xlim, set_ylim y set_zlim se utilizan para establecer los límites de los ejes, 
asegurando que el vector sea visible en el gráfico. Las etiquetas de los ejes se añaden para una mejor comprensión del gráfico."""