#2. Realice un programa que le permita al usuario ingresar los coeficientes de una función de transferencia de segundo orden y graficar su comportamiento, 
#además se debe mostrar que tipo de sistema es: subamortiguado, criticamente amortiguado y sobreamortiguado.
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step
# Solicitar al usuario los coeficientes de la función de transferencia
K = float(input("Ingrese la ganancia: "))
wn = float(input("Ingrese la frecuencia natural: "))
zita = float(input("Ingrese el factor de amortiguamiento: "))

# num = [float(input("Ingrese el coeficiente del numerador (K): "))]
# den = [
#     float(input("Ingrese el coeficiente de s^2: ")),
#     float(input("Ingrese el coeficiente de s: ")),
#     float(input("Ingrese el término constante: "))
# ]

# Crear la función de transferencia
sistema = lti([K*pow(wn,2)], [1, 2*zita*wn, pow(wn,2)])
# Determinar el tipo de sistema basado en el factor de amortiguamiento ζ (zeta)

if zita < 1:
    print("El sistema es subamortiguado.")
elif zita == 1:
    print("El sistema es críticamente amortiguado.")
else:
    print("El sistema es sobreamortiguado.")
# Graficar la respuesta al escalón del sistema

t, y = step(sistema)
plt.plot(t, y)
plt.title('Respuesta al escalón de la función de transferencia')
plt.xlabel('Tiempo (s)')
plt.ylabel('Respuesta')
plt.grid()
plt.show()

"""utiliza las bibliotecas numpy, matplotlib.pyplot y scipy.signal para crear y analizar la función de transferencia. 
El usuario debe ingresar los coeficientes del numerador y del denominador cuando se le solicite. 
Luego, el programa calcula el factor de amortiguamiento ( \zeta ) y determina el tipo de sistema. Finalmente, grafica la respuesta al escalón del sistema."""
