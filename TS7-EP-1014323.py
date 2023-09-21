#Introduccion a la programacion
#21/09/2023
print("Eilyn Michelle Parada Vasquez")
while True:
    try:
        numero = int(input("Por favor, ingresa un número del 1 al 10: "))
        if 1 <= numero <= 10:
            for i in range(1, 11):
                resultado = numero * i
                print(f"{numero} x {i} = {resultado}")
            opcion = input("¿Deseas generar la tabla de otro número? (s/n): ")
            if opcion.lower() != 's':
                break
        else:
            print("El número debe estar en el rango del 1 al 10. Intenta nuevamente.")
    except ValueError:
        print("Por favor, ingresa un número válido.")