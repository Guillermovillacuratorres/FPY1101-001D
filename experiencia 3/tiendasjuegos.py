juegos = []


def crear_venta(id_juego:int, cantidad:int):
    juego_encontrado = buscar_juego(id_juego)
    if juego_encontrado != None:
        juegos[juego_encontrado]["cantidad_juego"] -= cantidad
        print("Venta realizada corectamente!")



def validar_stock(id_juego:int, cantidad:int):
    juego_encontrado = buscar_juego(id_juego)
    if juego_encontrado != None:
        #                               10                  5
        if juegos[juego_encontrado]["cantidad_juego"] < cantidad:
            return False
        else:
            return True


def actualizar_juego(posicion:int,nombreJuego:str,precioJuego:int, cantidadJuego:int, generoJuego:str):
    juegos[posicion]["nombre_juego"] = nombreJuego
    juegos[posicion]["precio_juego"] = precioJuego
    juegos[posicion]["cantidad_juego"] = cantidadJuego
    juegos[posicion]["genero_juego"] = generoJuego
    print("Juego actualizado correctamente")
    


def eliminar_juego(posicion:int):
    juegos.pop(posicion)
    print("El juego se elimino correctamente!")



def buscar_juego(id_juego:int)->int | None:
    contador=0
    for i in juegos:
        if i["id_juego"] == id_juego:
            return contador
        contador+=1


def mostrar_juegos():
    if len(juegos) == 0:
        print("No hay juegos registrados.")
    else:
        for i in juegos:
            print("NOMBRE: ",i["nombre_juego"],"-","PRECIO: $",i["precio_juego"],"-", "CANTIDAD: ",i["cantidad_juego"] )

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

            juego_encontrado = buscar_juego(id_juego)

            if juego_encontrado == None:
                nombre_juego = validar_string("Ingrese el nombre del juego: ")
                precio_juego = validar_entero_positivo("Ingrese el precio del juego: ")
                cantidad_juego = validar_entero_positivo("Ingrese la cantidad de juegos: ")
                genero_juego = validar_string("Ingrese el genero del juego: ")

                agregar_juego(id_juego, nombre_juego, precio_juego, cantidad_juego, genero_juego)
            else:
                print("EL id del juego ya se encuentra registrado.")
        elif opc == 2:
            mostrar_juegos()


        elif opc == 3:
            id_juego = validar_entero_positivo("Ingrese el id del juego a vender: ")
            juego_encontrado = buscar_juego(id_juego)

            if juego_encontrado == None:
                print("EL juego no se encontro.")
            else:
                cantidad_vender = validar_entero_positivo("Ingrese la cantidad de juegos a vender: ")
                venta_valida = validar_stock(id_juego,cantidad_vender)
                if venta_valida == True:
                    crear_venta(id_juego,cantidad_vender)
                else:
                    print("No hay stock")


        elif opc == 4:
            pedir_juego_id=validar_entero_positivo("Ingrese el id del juego: ")
            juego_encontrado=buscar_juego(pedir_juego_id)

            if juego_encontrado == None:
                print("Juego no encontrado")
            else:
                eliminar_juego(juego_encontrado)


        elif opc == 5:
            id_juego = validar_entero_positivo("Ingrese el id del juego a editar: ")

            juego_encontrado = buscar_juego(id_juego)

            if juego_encontrado == None:
                print("El juego no se encontró")
            else:
                nombre_juego = validar_string("Ingrese el nombre del juego: ")
                cantidad_juego = validar_entero_positivo("Ingrese la cantidad del juego: ")
                genero_juego = validar_string("Ingrese el genero del juego: ")
                precio_juego = validar_entero_positivo("Ingrese el precio del juego: ")

                actualizar_juego(juego_encontrado,nombre_juego,precio_juego,cantidad_juego,genero_juego)


menu()
