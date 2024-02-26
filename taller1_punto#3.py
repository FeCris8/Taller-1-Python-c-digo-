#3. Realice un programa que convierta coordenadas rectangulares a cilíndricas y esféricas, para lo cual deben consultar sobre el uso de funciones trigonométricas en Python:
import numpy as np
def rectangular_a_cilindricas(x, y, z):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return rho, phi, z
def rectangular_a_esfericas(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arctan2(np.sqrt(x**2 + y**2), z)
    phi = np.arctan2(y, x)
    return r, theta, phi
# Coordenadas rectangulares
x, y, z = 7, 14, 21
# Conversión a coordenadas cilíndricas
rho, phi, z_cilindrica = rectangular_a_cilindricas(x, y, z)
print(f"Coordenadas cilíndricas: rho={rho}, phi={phi}, z={z_cilindrica}")
# Conversión a coordenadas esféricas
r, theta, phi_esferica = rectangular_a_esfericas(x, y, z)
print(f"Coordenadas esféricas: r={r}, theta={theta}, phi={phi_esferica}")

"""En este código, np.sqrt se utiliza para calcular la raíz cuadrada y np.arctan2 para calcular el ángulo ( \phi ) en radianes, que es una versión segura de la función arco tangente 
que maneja correctamente los cuadrantes. La función rectangular_a_cilindricas convierte las coordenadas rectangulares a cilíndricas, y la función rectangular_a_esfericas las
convierte a esféricas.
Recuerdar que en las coordenadas cilíndricas, ( \rho ) es la distancia radial desde el eje z, ( \phi ) es el ángulo azimutal y z es la misma coordenada z. En las coordenadas esféricas,
( r ) es la distancia radial desde el origen, ( \theta ) es el ángulo polar (o colatitud), y ( \phi ) es el ángulo azimutal."""
