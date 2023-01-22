"""
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.
"""
area = int(input("Digite a área a ser pintada em m²: "))

litros = area//3 #A quantidade de litros necessárias para pintar pelo menos 3 metros quadrados da aŕea a ser pintada
if area % 3 > 0: #Resto da divisão for maior que zero. Para verificar se há resto de tinta que não foi utilizada.
    litros = litros + 1 #irá somar a quantidade de litros necessárias para pintar a área + 1

latas = litros//18 # Divisão inteira para dizer quantas latas precisam ser compradas
if litros % 18 > 0:#Resto da divisão é maior que zero. Significa que que precisa comprar uma lata a mais. mesmo que não use ela toda
    latas = latas + 1#Soma da quantidade de latas que precisa comprar somado a mais uma lata para pintar a área

print("Você precisara de", latas, "lata(s).")
print("Você vai pagar R$", latas*80,"reais") #Cada lata custa 80 reais. Para saber o total, multiplica a quantidade de latos pelo seu valor unitário
