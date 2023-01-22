#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Qual o preço do produto? R$'))

desconto = preco - (preco * 5/100)

print('O produto que custava R${}. Na promoção com 5% de desconto vai passar a custar R${:.2f}'.format(preco, desconto))