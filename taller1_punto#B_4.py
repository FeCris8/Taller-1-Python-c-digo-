#4. Realice un programa que le permita al usuario escoger entre robot Cilíndrico, Cartesiano y esférico, donde como respuesta a la selección conteste con el tipo y número de articulaciones que posee.
def informacion_robot(tipo):
    if tipo.lower() == 'cilindrico':
        return "Robot Cilíndrico: posee una articulación rotacional sobre una base y articulaciones lineales para el movimiento en altura y en radio."
    elif tipo.lower() == 'cartesiano':
        return "Robot Cartesiano: también conocido como robot rectilíneo, tiene tres articulaciones lineales que se mueven en los ejes X, Y y Z."
    elif tipo.lower() == 'esferico':
        return "Robot Esférico: cuenta con dos articulaciones rotacionales y una lineal."
    else:
        return "Tipo de robot no reconocido. Por favor, elija entre 'cilindrico', 'cartesiano' o 'esférico'."
# Solicitar al usuario que ingrese el tipo de robot
tipo_robot = input("Ingrese el tipo de robot (cilindrico, cartesiano, esférico): ")
# Mostrar la información del robot seleccionado
print(informacion_robot(tipo_robot))

"""Este programa define una función informacion_robot que toma como argumento el tipo de robot y devuelve una cadena de texto con la descripción del tipo y número de articulaciones.
 Luego, solicita al usuario que ingrese el tipo de robot y muestra la información correspondiente.
Recuerda que los robots cilíndricos son adecuados para operaciones de ensamblaje y manejo de materiales, los cartesianos son ideales para tareas de alta precisión como el CNC y 
la impresión 3D, y los esféricos se utilizan comúnmente en aplicaciones de soldadura y ensamblaje"""
