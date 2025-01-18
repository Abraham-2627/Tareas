print("Este programa determina el mayor número de tres que introduzcas.")

while True:
    # Preguntar al usuario si desea continuar
    respuesta_usuario = input("¿Quieres continuar? (si/no): ").strip().lower()
    
    if respuesta_usuario == "sí" or respuesta_usuario == "si":
        # Solicitar los tres números al usuario
        while True:
            try:
                primer_numero = float(input("Introduce el primer número: "))
                segundo_numero = float(input("Introduce el segundo número: "))
                tercer_numero = float(input("Introduce el tercer número: "))
                break  # Salimos del bucle si los números son válidos
            except ValueError:
                print("No escribiste un valor numérico. Por favor, ingresa un número válido.")

        # Determinar el mayor número
        numero_mayor = max(primer_numero, segundo_numero, tercer_numero)
        print(f"El mayor de los números es: {numero_mayor}")
    
    elif respuesta_usuario == "no":
        print("Okay, nos vemos en otra ocasión.")
        break  # Salimos del programa

    else:
        print("Por favor, responde solo 'si' o 'no'.")
