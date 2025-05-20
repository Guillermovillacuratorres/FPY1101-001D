while True:
    try:
        edad = int(input("Ingrese su edad:"))
    except ValueError as e:
        print(e)
        #print("Error, el campo de la edad, solo recibe numeros enteros.")
    except TypeError as e:
        print(e)
    else:
        print("No hay ningun error en el try!!!")
        break
    finally:
        print("Siempre estoy en todo!!!")