#C. Uso de las funciones para graficar
#1. Realice un programa que grafique el comportamiento de un sensor PT100 desde -200°C a 200°C.
import matplotlib.pyplot as plt
import numpy as np
# Coeficientes de la ecuación de Callendar-Van Dusen para PT100
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12
# Función para calcular la resistencia de un PT100 en función de la temperatura
def resistencia_PT100(temperatura):
    if temperatura >= 0:
        return 100 * (1 + A * temperatura + B * temperatura**2)
    else:
        return 100 * (1 + A * temperatura + B * temperatura**2 + C * (temperatura - 100) * temperatura**3)
# Rango de temperaturas desde -200°C a 200°C
temperaturas = np.linspace(-200, 200, 400)
resistencias = [resistencia_PT100(t) for t in temperaturas]
# Crear gráfico
plt.figure(figsize=(10, 5))
plt.plot(temperaturas, resistencias, label='Resistencia PT100')
plt.title('Comportamiento del sensor PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ω)')
plt.legend()
plt.grid(True)
plt.show()
"""define una función resistencia_PT100 que calcula la resistencia de un sensor PT100 en función de la temperatura utilizando 
la ecuación de Callendar-Van Dusen. Luego, genera un conjunto de temperaturas entre -200°C y 200°C, calcula las resistencias correspondientes
 y las grafica utilizando matplotlib."""