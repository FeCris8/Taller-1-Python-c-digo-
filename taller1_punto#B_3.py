#3. Realice un programa para el cálculo de volúmenes (Prisma, Pirámide, Cono truncado, Cilindro) donde el usuario pueda seleccionar el sólido y los parámetros de cada volumen.
import math
def volumen_prisma(base, altura, profundidad):
    return base * altura * profundidad
def volumen_piramide(base, altura):
    return (1/3) * base * altura
def volumen_cono_truncado(radio_mayor, radio_menor, altura):
    return (1/3) * math.pi * altura * (radio_mayor**2 + radio_menor**2 + radio_mayor * radio_menor)
def volumen_cilindro(radio, altura):
    return math.pi * radio**2 * altura
def calcular_volumen():
    print("Seleccione el sólido para calcular su volumen:")
    print("1. Prisma")
    print("2. Pirámide")
    print("3. Cono truncado")
    print("4. Cilindro")
    opcion = int(input("Ingrese el número del sólido seleccionado: "))
    if opcion == 1:
        base = float(input("Ingrese la base del prisma: "))
        altura = float(input("Ingrese la altura del prisma: "))
        profundidad = float(input("Ingrese la profundidad del prisma: "))
        print("El volumen del prisma es:", volumen_prisma(base, altura, profundidad))
    elif opcion == 2:
        base = float(input("Ingrese la base de la pirámide: "))
        altura = float(input("Ingrese la altura de la pirámide: "))
        print("El volumen de la pirámide es:", volumen_piramide(base, altura))
    elif opcion == 3:
        radio_mayor = float(input("Ingrese el radio mayor del cono truncado: "))
        radio_menor = float(input("Ingrese el radio menor del cono truncado: "))
        altura = float(input("Ingrese la altura del cono truncado: "))
        print("El volumen del cono truncado es:", volumen_cono_truncado(radio_mayor, radio_menor, altura))
    elif opcion == 4:
        radio = float(input("Ingrese el radio del cilindro: "))
        altura = float(input("Ingrese la altura del cilindro: "))
        print("El volumen del cilindro es:", volumen_cilindro(radio, altura))
    else:
        print("Opción no válida. Por favor, seleccione un número entre 1 y 4.")
# Llamar a la función para ejecutar el programa
calcular_volumen()

"""un menú simple para que elija entre un prisma, una pirámide, un cono truncado o un cilindro. Luego, solicita los parámetros 
necesarios y calcula el volumen correspondiente. Recuerda que las fórmulas utilizadas para calcular los volúmenes son aproximaciones y asumen que las figuras 
son perfectas y están bien definidas."""
