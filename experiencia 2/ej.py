MOTOCICLETAS = 500
AUTO = 1000
CAMION = 2500

contador_motocicletas = 0
contador_auto = 0
contador_camion = 0

acumulador_motocicletas = 0
acumulador_auto = 0
acumulador_camion = 0

while True:
    print("[1] - Registrar Motocicleta ($500)")
    print("[2] - Registrar Auto ($1.000)")
    print("[3] - Registrar Camión ($2.500)")
    print("[4] - Salir y mostrar reporte")

    while True:
        try:
            opc = int(input("Seleccione una opcion: "))
            if opc < 1 or opc >4:
                print("Solo existen 4 opciones (1-2-3-4)")
            else:
                break
        except ValueError as e:
            print("Solo se permiten numeros")

    
    if opc == 1:
        
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de motos:"))
                if cantidad <= 0:
                    print("No se aceptan numeros negativos.")
                else:
                    break
            except:
                print("Solo se aceptan numeros enteros.")

        for i in range(cantidad):
            while True:
                patente = input("Ingrese su patente:")
                if len(patente) <= 0:
                    print("La patente no debe estar vacia.")
                elif len(patente) > 5:
                    print("El largo de la patenet permitido es 5 caracteres")
                else:
                    break

            contador_motocicletas += 1
            acumulador_motocicletas += MOTOCICLETAS
            
                

    
    if opc == 2:
        print("opc 1")
    
    if opc == 3:
        print("opc 1")

    if opc == 4:
        print(f"Pasaron {contador_motocicletas} motocicletas con un total de $ {acumulador_motocicletas}")

        break