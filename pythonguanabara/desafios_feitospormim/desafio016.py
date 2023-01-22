"""Crie um programa que leia um número Real qualquer pelo teclado
 e mostra na tela a sua porção inteira.
 Ex: Digite um número:6.127
 O número 6.127 tem a parte inteira 6."""

import math #importa todos os módulos da biblioteca math

num = float(input('Digite um número:'))

inteiro = math.trunc(num)
print('O número {} tem a parte inteira {:.0f}'.format(num, inteiro))

