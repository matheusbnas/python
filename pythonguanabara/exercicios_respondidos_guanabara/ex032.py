"""Faça um programa que leia um ano qualquer e mostre seu ano BISSEXTO"""

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #Diz o ano atual na qual estamos e analisa se é bissexto ou não.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #O resto da divisão por 4 e 100 é igual a 0 e diferente de 0 espectivamente. Ou o resto da divisão por 400 é igual a 400.
    print('O ano {} é  BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
