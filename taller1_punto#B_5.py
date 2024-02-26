#5. Escribir un programa que realice la pregunta ¿Desea continuar Si/No? y que no deje de hacerla hasta que el usuario teclee No. 
while True:
    respuesta = input("¿Desea continuar Si/No? ").lower()
    if respuesta == "no":
        break

"""Este bucle while seguirá ejecutándose hasta que el usuario escriba “No”. La función input recoge la respuesta del usuario y la convierte a minúsculas con .lower() 
para que el programa funcione independientemente de cómo el usuario escriba su respuesta. Cuando el usuario teclea “No”, el bucle se rompe y el programa termina."""
