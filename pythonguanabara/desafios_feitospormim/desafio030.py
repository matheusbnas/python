"""Crie um programa que leia um número inteiro e mostre na tela
se ele é PAR ou ÍMPÁR."""

num = int(input("Entre com um número inteiro: "))

if num % 2 == 0:
    print("O número {} é par".format(num))
else:
    print("O número {} é ímpar".format(num))
