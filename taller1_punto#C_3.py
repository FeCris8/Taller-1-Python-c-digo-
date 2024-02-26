#3. Implemente la ecuación de carga y descarga para un circuito RC. El usuario ingresa por teclado el valor de voltaje (V), capacitancia (𝜇𝐹) y resistencia (Ω).
#Posteriormente realice en Python la gráfica. 
import numpy as np
import matplotlib.pyplot as plt
# Solicitar al usuario que ingrese los valores de voltaje, capacitancia y resistencia
V = float(input("Ingrese el valor del voltaje (V): "))
C = float(input("Ingrese el valor de la capacitancia (μF): ")) * 1e-6  # Convertir μF a F
R = float(input("Ingrese el valor de la resistencia (Ω): "))
# Definir la constante de tiempo τ (tau)
tau = R * C
# Definir el tiempo de simulación y el paso de tiempo
t = np.linspace(0, 5 * tau, 1000)
# Ecuaciones de carga y descarga
Vcarga = V * (1 - np.exp(-t / tau))
Vdescarga = V * np.exp(-t / tau)
# Graficar
plt.figure(figsize=(10, 5))
plt.plot(t, Vcarga, label='Carga del Capacitor')
plt.plot(t, Vdescarga, label='Descarga del Capacitor')
plt.title('Carga y Descarga de un Circuito RC')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.legend()
plt.grid(True)
plt.show()

"""utiliza la biblioteca numpy para manejar los cálculos numéricos y matplotlib para graficar. 
Las ecuaciones de carga y descarga del capacitor en un circuito RC son ( V(t) = V(1 - e^{-\frac{t}{RC}}) ) 
para la carga y ( V(t) = Ve^{-\frac{t}{RC}} ) 
para la descarga, donde ( V ) es el voltaje inicial, ( R ) es la resistencia, ( C ) es la capacitancia, ( t ) es el tiempo y ( e ) es la base del logaritmo natural."""