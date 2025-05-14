while True:
    try:
        edad = int(input("Ingrese su edad:"))
        altura = float(input("Ingrese su altura:"))
    except ValueError as e:
        print(f"Error, solo puedes ingresar números.")
    else:
        break
    finally:
        print("Siempre me ejecuto!!!!!")
