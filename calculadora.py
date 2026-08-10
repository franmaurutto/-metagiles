def sumar(numeros):
    if numeros == "":
        return 0
    numeros = numeros.split(",")

    if len(numeros) == 1:
        return int(numeros[0])

    return int(numeros[0]) + int(numeros[1])