#Atravessar rua

def atravessar_rua(nome, idade):


    if idade > 18:
        return f'Pode atravessar {nome}. Sua idade de {idade} anos é permitida!'
    elif idade <= 14 :
        return f'Jamais atravesse sozinho(a) {nome} com {idade} anos'
    else:
        return f'Pode atravessar {nome}, mas sempre alguém por perto devido a sua idade de {idade} anos'

n = str(input('Dia seu nome: '))
id = int(input('Identifique sua idade: '))
print(atravessar_rua(n, id))