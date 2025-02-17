
#Constante de la proporción áurea
phi = 1.618

#Partes del cuerpo (por ejemplo, longitud del brazo y antebrazo en cm)
parte_mayor = int(input("dime cuanto mide tu brazo entero en CM: " ))  # Cambia este valor
parte_menor = int(input("dime cuanto mide de tu mano a tu codo en CM: "))  # Cambia este valor

#Calcular la proporción
proporcion = parte_mayor / parte_menor

#Calcular la diferencia con respecto a Phi
diferencia = abs(proporcion - phi)

#Mostrar resultados
print(f"Proporción calculada: {proporcion:.3f}")
print(f"Diferencia con Phi: {diferencia:.3f}")

#Evaluación de cercanía
if diferencia < 0.05:  # Umbral ajustable
    print("¡La proporción está muy cerca de Phi!")
else:
    print("La proporción no es tan cercana a Phi.")


