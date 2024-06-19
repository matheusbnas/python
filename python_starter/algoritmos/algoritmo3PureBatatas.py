#Algortimo de purê de batatas
#Abrir a geladeira
def abrir_geladeira(qtd_batatas):

    batatas_receita = 10
    z = batatas_receita - qtd_batatas
    if z > 0:
        print(f'Quantidade de batatas faltantes para fazer purê de batata são {z}. Precisa fazer compras no mercado.')
        print()
        return fazer_compras(z)
    else:
        return print("Tenho a quantidade necessária para fazer purê de batatas")


#comprar batatas se a qtd de batatas para.
def fazer_compras(batatas_faltantes):
    print(".....Pegar a carteira.....")
    print("......Ir para o mercado fazer compras......")
    print('Enquanto isso vou comprando batatas no mercado.')
    print()

    qtd_batatas = 0
    batatas_compradas = []
    while qtd_batatas < batatas_faltantes:
        batatas_compradas.append(qtd_batatas)
        print(batatas_compradas)
        qtd_batatas += 1
        if qtd_batatas == batatas_faltantes:
            print("......Indo para casa......")
            print(f'Comprei as {len(batatas_compradas)} batata(s) que faltavam. Agora posso ir para casa.')
    
    return None

qtd_batatas = int(input("Quantas batatas há na geladeira: "))
abrir_geladeira(qtd_batatas)