"""Faça um programa um programa que leia um número
de 0 a 9999 e mostre na tela cada um dos digitos
separados

Ex: Digite um número:1834

unidade:4
dezena:3
centena:8
milhar:1"""

numero = int(input("Informe um número: "))
u = numero // 1 % 10 #acha o resto da divisão do numero inteiro. Assim, dizendo o numero respectivo de acordo com sua unidade.
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print("Analisando o número {}".format(numero))
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

#n = input('Insira um número: ').zfill(4)

#print('Unidades: {} \nDezenas: {} \nCentenas: {} \nMilhares: {}'.format(n[-1:], n[-2:-1], n[-3:-2], n[0]))


#num = str(int(input('Digite um número entre 0 e 9999: '))+10000)
#print('unidade...: {} \ndezena....: {} \ncentena...: {} \nmilhar....: {}'.format(num[4],num[3],num[2],num[1]))﻿

#num=str(input('Digite um numero de 0 a 9999: ')).zfill(4)
#print('O numero digitado foi: {}',num)
#print('Unidade: {}'.format(num[3]))
#print('Dezena: {}'.format(num[2]))
#print('Centena: {}'.format(num[1]))
#print('Milhar: {}'.format(num[0]))
