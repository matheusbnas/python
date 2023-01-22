"""Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""

from math import sin,cos,tan
angulo = float(input('Digite um ângulo: '))

print('O seno de {} é: {}'.format(angulo,sin(angulo)))
print('O cosseno de {} é: {}'.format(angulo,cos(angulo)))
print('A tangente de {} é: {}'.format(angulo,tan(angulo)))