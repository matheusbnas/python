def contar_caracteres(s): #Contar quantos caracteres de uma determinada letra aparece na lista
    """Funcao que conta os caracteres de uma String
    Ex:

    >>> contar_caracteres('emerson')
    {'e': 2, 'm': 1, n: 1, 'o': 1, 'r': 1, 's': 1}
    >>> contar_caracteres('banana')
    {'a':3,'b':1, 'n':2}

    :param s: string a ser contada
    """

    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter] = contagem

    return resultado

    print(f'{primeiro_caracter}: {contagem}')

if __name__ == '__main__':
    print(contar_caracteres('amanda'))
    print()
    print(contar_caracteres('banana'))