#Crie um programa que leia quanto de dinheiro tem n carteira e mostre quantos Dólares ela pode comprar.
#Considerar: US$1.00 = R$3.27

money = float(input("Quanto de dinheiro tem na carteira? R$ "))

dolar_em_reais = money / 3.27


print('Com R${} você pode comprar US${}'.format(money,dolar_em_reais))

