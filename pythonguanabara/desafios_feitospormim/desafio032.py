"""Faça um programa que leia um ano qualquer e mostre seu ano BISSEXTO"""

ano = int(input('Escreva o ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Bissexto')
else:
    print('Não é bissexto')
