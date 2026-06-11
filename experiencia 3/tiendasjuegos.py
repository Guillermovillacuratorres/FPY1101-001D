juegos = []
def buscar_juego(id_juego:int)->int | None:
    contador=0
    for i in juegos:
        if i["id_juego"] == id_juego:
            return contador
        contador+=1
def eliminar_juego():
    pedir_juego_id=validar_entero_positivo("Ingrese el id del juego: ")
    juego_encontrado=buscar_juego(pedir_juego_id)

    if juego_encontrado == None:
        print("Juego no encontrado")
    else:
        juegos.pop(juego_encontrado)



def mostrar_juegos():
    for i in juegos:
        print(i["nombre_juego"],"-",i["precio_juego"],"-", i["cantidad_juego"] )

def agregar_juego(idjuego: int,nombrejuego: str, preciojuego: int, cantidadjuego: int, generojuego: str):
    diccionario = {
        "id_juego":idjuego,
        "nombre_juego":nombrejuego,
        "precio_juego":preciojuego,
        "cantidad_juego":cantidadjuego,
        "genero_juego":generojuego
    }
    juegos.append(diccionario)

def validar_string(msj:str):
    while(True):
        valor=input(msj);
        if(len(valor)<3):
            print("El nombre ingresado es muy corto (largo mínimo es 3)")
            continue
        if valor.isalpha()==False:
            print("No puede contener números o espacios en blanco")
            continue
        else:
            return valor

def validar_entero_positivo(mensaje:str):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            elif valor == 0:
                print("No se puede ingresar un 0")
            else:
                print("El numero tiene que ser un entero positivo")
        except:
            print("No se permiten letras ni caracteres especiales")
            continue
def menu():
    while True:
        print("1- Registro juego")
        print("2- Mostrar juegos")
        print("3- Crear venta")
        print("4- Eliminar juego")
        print("5- Actualizar juego")
        print("6- Salir")
        opc = validar_entero_positivo("Ingrese una opcion : ")
        if opc == 1:
            id_juego = validar_entero_positivo("Ingrese el id del juego: ")
            nombre_juego = validar_string("Ingrese el nombre del juego: ")
            precio_juego = validar_entero_positivo("Ingrese el precio del juego: ")
            cantidad_juego = validar_entero_positivo("Ingrese la cantidad de juegos: ")
            genero_juego = validar_string("Ingrese el genero del juego: ")

            agregar_juego(id_juego, nombre_juego, precio_juego, cantidad_juego, genero_juego)
        if opc == 2:
            mostrar_juegos()
menu()
