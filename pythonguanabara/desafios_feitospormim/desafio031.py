"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km
e R$0,45 para viagens mais longas."""

viagem = float(input("Qual foi a distância da viagem? "))

preco = 0.50 * viagem
preco1 = 0.45 * viagem

if viagem <= 200:
    print("O preço da passagem é: R${:0.2f}".format(preco))
else:
    print("O preço da passagem é: R${:0.2f}".format(preco1))
