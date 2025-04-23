"""tabla = int(input("Ingrese la tabla de multiplicar:"))
cantidaTabla = int(input("Ingrese la cantida de numeros a multiplicar:"))
for i in range(cantidaTabla):
    print(f"{i+1} X {tabla} = {(i+1) * tabla}")"""


texto = "Hola, me llamo Pedro, como estás?"

contador = 0
for letra in texto:
    contador +=1
    if letra.lower() == 'p':
        print("Encontramos la p, que esta en la posicion: ", texto.find(letra))
        print("Verifico la posicion de la letra: ", texto[15])