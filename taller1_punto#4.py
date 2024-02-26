#4. Realice un programa para el cálculo de la resistencia de una RTD de platino (PT100) en función de la temperatura:
def calcular_resistencia_pt100(temperatura):
    # Constantes para la ecuación de Callendar-Van Dusen
    R0 = 100.0  # Resistencia de la PT100 a 0°C
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12  # Solo se usa si la temperatura es menor a 0°C
    if temperatura >= 0:
        # Ecuación para temperaturas mayores o iguales a 0°C
        resistencia = R0 * (1 + A * temperatura + B * temperatura**2)
    else:
        # Ecuación para temperaturas menores a 0°C
        resistencia = R0 * (1 + A * temperatura + B * temperatura**2 + C * (temperatura - 100) * temperatura**3)
    return resistencia
#Ejemplo 
temperatura = 0  # Temperatura en °C
resistencia = calcular_resistencia_pt100(temperatura)
print(f"La resistencia de la PT100 a {temperatura}°C es: {resistencia} ohms")

"""Este programa define una función calcular_resistencia_pt100 que toma como argumento la temperatura en grados Celsius y devuelve la resistencia correspondiente de la RTD PT100.
 La ecuación utilizada es válida para el rango de temperatura estándar de las RTD de platino según la norma IEC 607511. Para temperaturas por debajo de 0°C, 
 se utiliza una ecuación modificada que incluye un término adicional con la constante C."""