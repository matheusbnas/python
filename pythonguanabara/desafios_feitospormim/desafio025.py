"""Crie um programa que leia o nome de uma pessoa
e diga se ela tem Silva no nome"""

nome = input("Qual é seu nome completo?").strip().upper()

sobrenome = 'SILVA' in nome

print(nome)
print("Seu nome tem Silva? {}".format(sobrenome))