"""Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa."""

from math import pow,sqrt #importa da biblioteca math somente os módulos pow e sqrt(raiz quadrada)

cateto_oposto = float(input('O comprimento do cateto oposto é:'))
cateto_adjacente = float(input('O comprimento do cateto adjacente é:'))

hipotenusa = sqrt(pow(cateto_oposto,2) + pow(cateto_adjacente,2)) #pow siginifica ex

print('O comprimento da hipotenusa é: {}'.format(hipotenusa))
