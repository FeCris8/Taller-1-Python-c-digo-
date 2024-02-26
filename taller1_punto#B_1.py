#B. Con interacción de consola (fprintf o disp) y teclado (input)
#1. Realice un programa que calcule la potencia que consume un circuito ingresando por teclado el valor de corriente y voltaje.

def calcular_potencia():
    # Solicitar al usuario que ingrese el valor de la corriente (en amperios)
    corriente = float(input("Ingrese el valor de la corriente (en amperios): "))    
    # Solicitar al usuario que ingrese el valor del voltaje (en voltios)
    voltaje = float(input("Ingrese el valor del voltaje (en voltios): "))    
    # Calcular la potencia usando la fórmula P = V * I
    potencia = voltaje * corriente    
    # Mostrar el resultado
    print(f"La potencia consumida por el circuito es: {potencia} watts")
# Llamar a la función para ejecutar el programa
calcular_potencia()

"""" define una función calcular_potencia que solicita al usuario ingresar los valores de corriente y voltaje. 
Luego calcula la potencia consumida utilizando la fórmula ( P = V \times I ), donde ( P ) es la potencia en watts, ( V ) es el voltaje en voltios y 
( I ) es la corriente en amperios. Finalmente, muestra el resultado en la consola."""
