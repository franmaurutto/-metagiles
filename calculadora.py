def sumar(numeros):
    if numeros == "":
        return 0
    numeros = numeros.split(",")

    return sum(int(numero) for numero in numeros)