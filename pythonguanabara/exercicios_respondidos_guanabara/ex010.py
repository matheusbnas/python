#Crie um programa que leia quanto de dinheiro tem n carteira e mostre quantos Dólares ela pode comprar.
#Considerar: US$1.00 = R$3.27

real = float(input("Quanto de dinheiro você tem na carteira? R$ "))

dolar_em_reais = real / 3.27

print('Com R${} você pode comprar US${}'.format(real,dolar_em_reais))