"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias
    int()
    //
    %
    if
"""

area_pintada = int(input("Digite a área a ser pintada em m²: "))

litros = area_pintada // 6
if area_pintada % 6 > 0: #Resto da divisão for maior que zero. Feito esse cálculo para verificar que ainda há um resto que não foi suprida.
    litros = litros + 1 #irá somar litros + 1

print("Quantos litros de tinta será necessário para pintar a parede? {}L".format(litros))
print()

latas = litros // 18
if litros % 18 > 0:
    latas = latas + 1

print('Você precisará de {} lata(s).'.format(latas))
print('Você vai pagar R$ {} se comprar somente latas'.format(latas*80))
print()

galoes = litros // 4
if litros % 4 > 0:
    latas = latas + 1


print('Você precisará de {} galoes'.format(galoes))
print('Você vai pagar R$ {} se comprar somente galões'.format(galoes*25))
print()

    if litros % 4 > 0 and  litros % 18 > 0:
        print('Você precisará de {} latas e {} galões. Caso desejar comprar em partes'.format(latas,galoes))
        print('Você vai pagar R$ {} se comprar galões e latas ao mesmo tempo'.format(latas*80 + galoes*25))
