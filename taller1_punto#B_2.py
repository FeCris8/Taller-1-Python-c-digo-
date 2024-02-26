#2. Realice un programa que calcule X números aleatorios en un rango determinado por el usuario.
import random
def generar_numeros_aleatorios(cantidad, rango_inicial, rango_final):
    numeros_aleatorios = [random.randint(rango_inicial, rango_final) for _ in range(cantidad)]
    return numeros_aleatorios
# Solicitar al usuario la cantidad de números aleatorios a generar
X = int(input("Ingrese la cantidad de números aleatorios que desea generar: "))
# Solicitar al usuario el rango de los números aleatorios
rango_inicial = int(input("Ingrese el valor inicial del rango: "))
rango_final = int(input("Ingrese el valor final del rango: "))
# Generar y mostrar los números aleatorios
numeros = generar_numeros_aleatorios(X, rango_inicial, rango_final)
print("Números aleatorios generados:", numeros)

"""define una función generar_numeros_aleatorios que toma como argumentos la cantidad de números aleatorios a generar y el rango inicial y final.
 Utiliza la función random.randint para generar cada número aleatorio. Luego, solicita al usuario que ingrese los valores necesarios y muestra los números aleatorios generados."""