"""Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa."""

co = float(input('O comprimento do cateto oposto:'))
ca = float(input('O comprimento do cateto adjacente:'))

h1 = (co**2 + ca**2) **(1/2)
print('A hipotenusa vai medir: {}'.format(h1))

import math

co = float(input('O comprimento do cateto oposto:'))
ca = float(input('O comprimento do cateto adjacente:'))

h1 = math.hypot(co,ca) #método da hipotenusa qu  o python já tem na biblioteca math
print('A hipotenusa vai medir: {}'.format(h1))