"""Crie um programa que leia o nome completo
de uma pessoa e mostre:

O nome como todas as letras maiusculas
O nome com todas as letras minusculas
Quantas letras ao todo(sem considerar espaços)
Quantas letras tem o primeiro nome"""

nome = str(input("Digite seu nome completo: ")).strip()

print("Analisando seu nome...")
print("Seu nome em letras maiúsculas é {}".format(nome.upper()))
print("Seu nome em letras minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))

separa = nome.split() #cria uma lista onde os caracteres sem letra fica com um espaço vazio(' ') entre as strings.
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
