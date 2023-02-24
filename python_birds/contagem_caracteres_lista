def contar_caracteres(s): #Contar quantos caracteres de uma determinada letra aparece na lista
    """Funcao que conta os caracteres de uma String
    Ex:

    >>> contar_caracteres('emerson')
    e: 2
    m: 1
    n: 1
    o: 1
    r: 1
    s: 1
    >>> contar_caracteres('banana')
    a:3
    b:1
    n:2
    
    :param s: string a ser contada
    
    """
    caracteres_ordenados = sorted(s) #Ordena os caracteres por ordem alfabética

    primeiro_caracter = caracteres_ordenados[0] #Defini como primeiro caracter
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == primeiro_caracter:
            contagem += 1
        else:
            print(f'{primeiro_caracter}: {contagem}')
            primeiro_caracter = caracter
            contagem = 1

    print(f'{primeiro_caracter}: {contagem}')

if __name__ == '__main__':
    contar_caracteres('emerson')
    print()
    contar_caracteres('banana')