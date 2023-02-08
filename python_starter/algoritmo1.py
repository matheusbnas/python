#Atravessar rua

def atravessar_rua(nome, idade):

    idade = int(input('Qual sua idade: '))

    if idade >= 18:
        return f'Pode atravessar {nome}.'
    elif  idade <= 14:
        return f'Jamais atravesse sozinho(a) {nome}'
    else:
        return f'Pode atravessar {nome}, mas sempre alguém por perto'

atravessar = atravessar_rua('Matheus', id)
print(atravessar)
