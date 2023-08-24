def soma(*parcelas): #Argumento de tupla
    print(parcelas)
    print(type(parcelas))

soma()
print()
soma(22)
print()
soma(23,45)

def soma(*parcelas): 
    print()
    aux = 0
    for valor in parcelas:
        aux += valor
    return print(aux)

soma()
print()
soma(14)
print()
soma(1,3,4)
