#Atravessar rua

def atravessar_rua(nome, idade):

    if idade >= 18:
        return f'Pode atravessar {nome}.'
    elif  idade <= 14:
        return f'Jamais atravesse sozinho(a) {nome}'
    else:
        return f'Pode atravessar {nome}, mas sempre alguém por perto'

n = str(input('Dia seu nome: '))
id = int(input('Identifique sua idade: '))
atravessar = atravessar_rua(n, id)
print(atravessar)
