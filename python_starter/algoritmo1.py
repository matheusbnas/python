#Atravessar rua

def atravessar_rua(adulto, crianca):

    idade = {adulto: 30, crianca: 7}

    if idade > 18:
        return 'Pode atravessar'
    elif  7 < idade < 18:
        return 'Pode atravessar, mas sempre alguém por perto'
    else:
        return 'Jamais atravesse sozinha'


atravessar = atravessar_rua(adulto=str, crianca=str)
print(atravessar)
