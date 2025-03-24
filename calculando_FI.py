

phi = 1.618


parte_mayor = int(input("dime cuanto mide tu brazo entero en CM: " ))
parte_menor = int(input("dime cuanto mide de tu mano a tu codo en CM: "))


proporcion = parte_mayor / parte_menor


diferencia = abs(proporcion - phi)


print(f"Proporción calculada: {proporcion:.3f}")
print(f"Diferencia con Phi: {diferencia:.3f}")


if diferencia < 0.05:
    print("¡La proporción está muy cerca de Phi!")
else:
    print("La proporción no es tan cercana a Phi.")


