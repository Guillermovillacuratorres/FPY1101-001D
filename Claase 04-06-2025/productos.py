datos = {
            "productos":
            [
                {
                    "id":1,
                    "nombre":"Audifonos",
                    "cantidad":10,
                    "precio":990
                },
                {
                    "id":2,
                    "nombre":"Parlante",
                    "cantidad":15,
                    "precio":500
                }
            ]
        }



while True:
    print("1 - Agregar productos")
    print("2 - Mostrar productos")
    print("3 - Buscar producto")
    print("4 - Editar producto")
    print("5 - Eliminar producto")
    print("6 - Salir")

    opcion = int(input("Ingrese una opcion:"))

    if opcion == 1:
        id = int(input("Ingrese un id del producto: "))
        nombre = input("Ingrese un nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = int(input("Ingrese el precio del producto: "))


        producto_agregar = {
                                "id":id,
                                "nombre":nombre,
                                "cantidad":cantidad,
                                "precio":precio
                            }
        datos["productos"].append(producto_agregar)
        print("Producto agregado correctamente.")
    elif opcion == 2:
        for i in datos["productos"]:
            print("NOMBRE : " + i["nombre"] + " CANTIDAD: " + str(i["cantidad"]) + " PRECIO: " + str(i["precio"])  )
            
    elif opcion == 3:
        id_producto = int(input("Ingrese el id del producto: "))
        for i in datos["productos"]:
            if i["id"] == id_producto:
                print(f"{i['id']} - {i['nombre']} - {i['cantidad']} - {i['precio']}")

    elif opcion == 4:
        id_producto = int(input("Ingrese el id del producto: "))
        for i in datos["productos"]:
            if i["id"] == id_producto:
                nombre = input("Ingrese un nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = int(input("Ingrese el precio del producto: "))
                i["nombre"] = nombre
                i["precio"] = precio
                i["cantidad"] = cantidad
                print("Producto editado correctamente!")
            
    elif opcion == 5:
        id_producto = int(input("Ingrese el id del producto: "))
        for i in datos["productos"]:
            if i["id"] == id_producto:
                datos["productos"].remove(i)
        


    else:
        print("Opcion no valida!")



print(datos["productos"])