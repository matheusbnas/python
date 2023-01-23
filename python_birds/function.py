#Atravessar rua

def atravessar_rua(crianca, adulto):

    usuario = ''
    usuario = int(input('Identifique o usuário atravessando a rua:'))

    if usuario == adulto:
        return 'Pode atravessar'
    elif usuario == (crianca > 10):
        return 'Pode atravessar, mas sempre alguém por perto'
    else:
        return 'Jamis atravesse sozinha'


print(atravessar_rua(c, a))

        
