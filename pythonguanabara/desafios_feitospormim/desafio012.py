#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Qual o preço do produto? R$'))

desconto = preco * (5/100)
preco_final = preco - desconto

print('O produto que custava R${}. Na promoção com 5% de desconto vai passar a custar R${}'.format(preco, preco_final))