#sin argumentos  - sin retorno
def sumar():
    """Esta funcion suma 1 + 1."""
    print(1+1)

#con argumentos  - sin retorno
def sumar(n1:int,n2:int):
    """Suma dos numeros y retorna el resultado."""
    print(n1+n2)

#sin argumentos  - con retorno
def sumar()->int:
    """Suma dos numeros y retorna el resultado."""
    return 1+1

#con argumentos  - con retorno
def sumar(n1:int,n2:int) -> int:
    """Suma dos numeros enteros y retorna la suma de ellos."""
    return(n1+n2)

#sin argumentos  - con retorno


sumar(90,90)
sumar()
sumar(1,20)
sumar()