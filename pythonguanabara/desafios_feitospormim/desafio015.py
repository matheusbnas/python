#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

preco_dias = 60 * dias
preco_km = 0.15 * km
total = preco_dias + preco_km

print('O total a pagar é de R${:.2f}'.format(total))
