#6. Realice un programa que calcule la fuerza de avance y retroceso de un cilindro neumático de doble efecto.
# Debe establecer previamente los valores de presión, así como las dimensiones físicas del cilindro para realizar el cálculo.
def calcular_fuerzas_cilindro(presion, diametro_cilindro, diametro_vastago):
    # Convertir presión de bar a Pascal para el cálculo (1 bar = 100000 Pascal)
    presion_pascal = presion * 100000    
    # Área del cilindro (pi * r^2)
    area_cilindro = 3.1416 * (diametro_cilindro / 2)**2    
    # Área del vástago (pi * r^2)
    area_vastago = 3.1416 * (diametro_vastago / 2)**2    
    # Fuerza de avance (Presión * Área del cilindro)
    fuerza_avance = presion_pascal * area_cilindro    
    # Fuerza de retroceso (Presión * (Área del cilindro - Área del vástago))
    fuerza_retroceso = presion_pascal * (area_cilindro - area_vastago)    
    # Convertir fuerza de Newton a kilogramos (1 N ≈ 0.10197 kg)
    fuerza_avance_kg = fuerza_avance * 0.10197
    fuerza_retroceso_kg = fuerza_retroceso * 0.10197    
    return fuerza_avance_kg, fuerza_retroceso_kg

# Ejemplo
presion_bar = 6  # Presión en bar
diametro_cilindro_mm = 100  # Diámetro del cilindro en mm
diametro_vastago_mm = 20  # Diámetro del vástago en mm
# Convertir mm a metros para el cálculo
diametro_cilindro_m = diametro_cilindro_mm / 1000
diametro_vastago_m = diametro_vastago_mm / 1000
fuerza_avance, fuerza_retroceso = calcular_fuerzas_cilindro(presion_bar, diametro_cilindro_m, diametro_vastago_m)
print(f"Fuerza de avance: {fuerza_avance} kg")
print(f"Fuerza de retroceso: {fuerza_retroceso} kg")


"""Este programa define una función calcular_fuerzas_cilindro que toma como argumentos la presión en bar, el diámetro del cilindro y el diámetro del vástago en metros,
 y devuelve la fuerza de avance y retroceso en kilogramos. La presión se convierte de bar a Pascal para el cálculo, y las fuerzas se calculan utilizando las áreas del cilindro y 
 del vástago. Finalmente, las fuerzas en Newton se convierten a kilogramos.
Recuerdar ajustar los valores de presion_bar, diametro_cilindro_mm y diametro_vastago_mm con los datos específicos de tu cilindro neumático. Además, 
ten en cuenta que este cálculo no incluye la fricción del cilindro, que puede afectar la fuerza real. Para un cálculo más preciso, considera reducir 
la fuerza teórica en un porcentaje que represente la fricción, que suele estar entre el 5% y el 10%"""