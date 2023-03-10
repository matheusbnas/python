#Abrir a geladeira
def abrir_geladeira(qtd_ovos):

    if qtd_ovos >= 4:
        return print('Pode fazer seu bolo')
    else:
        print('Quantidade de ovos é menor que 4. Precisa fazer compras no mercado')
        print()
        return fazer_compras(qtd_ovos)

#comprar ovos se a qtd  de ovos for menor que 4.
def fazer_compras(ovos):
    while ovos < 4:
        ovos += 1
        
    return print(f'Agora pode fazer o bolo com {ovos} ovos')

ovos = int(input("Quantos ovos há na geladeira: "))
abrir = abrir_geladeira(ovos)



