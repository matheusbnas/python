#Abrir a geladeira
def abrir_geladeira(qtd_ovos):

    if qtd_ovos >= 8:
        return print('Pode fazer seu bolo.')
    else:
        print('Quantidade de ovos é menor que 8. Precisa fazer compras no mercado.')
        print()
        return fazer_compras(qtd_ovos)

#comprar ovos se a qtd de ovos for menor que 8.
def fazer_compras(ovos):
    print("......fazendo compras......")
    print('Enquanto isso vou comprando ovos no mercado.')
    print()

    cartela_ovos = []
    while ovos < 8 and ovos > 0:
        ovos += 1
        cartela_ovos.append(ovos)
        print(cartela_ovos)
        if ovos == 8:
            print("......Indo para casa......")
            print(f'Comprei os {ovos} ovos. Agora posso ir para casa.')
    

    return fazer_bolo(cartela_ovos, tempo)

def fazer_bolo(caixa_ovos, tempo):

    if caixa_ovos == []:
        return print(f'caixa de ovos {caixa_ovos} em falta.')
    else: 
        while tempo:
            tempo += 1
            if tempo == 15:
                print()
                print(f'Tempo atual de cozimento: {tempo} minutos.')
                print("......fazendo o bolo......")
            elif tempo == 30:   
                print()
                print(f'Tempo atual de cozimento: {tempo} minutos.')
                print("......fazendo o bolo......")
            elif tempo == 45:
                print()
                print(f'Tempo atual de cozimento: {tempo} minutos.')
                print('Bolo está pronto :)')
ovos = int(input("Quantos ovos há na geladeira: "))
tempo = int(input("tempo de cozimento para preparar o bolo? "))
abrir_geladeira(ovos)



