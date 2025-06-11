def validar_numero_entero_positivo(mensaje_input:str="ingrese un numero: ") -> int:
    """Valida que numero sea entero y positivo."""
    while True:
        try:
            numero = int(input(mensaje_input))
            if numero < 0:
                print("Debe ingresar un numero positivo.")
                continue
        except ValueError:
            print("Debe ingresar un numero entero.")
            continue
        return numero
    

#edad = validar_numero_entero_positivo()
#print(edad)

def validar_texto(mensaje_input:str):
    """Valida el largo de un texto y verifica que no se encuentre vacio."""
    while True:
        texto = input(mensaje_input)
        if len(texto) == 0:
            print("El texto no puede estar vacio.")
            continue
        elif len(texto) > 1:
            print("El texto no puede ser mayor a un caracter.")
            continue
        else:
            return texto


letra = validar_texto("Ingrese A o B o C: ")
