"""Crie um programa que leia o nome completo
de uma pessoa e mostre:

O nome como todas as letras maiusculas
O nome com todas as letras minusculas
Quantas letras ao todo(sem considerar espaços)
Quantas letras tem o primeiro nome"""

nome = str(input("Digite seu nome completo: ")).strip()

maiscula = nome.upper()
minuscula = nome.lower()
total = len(nome) - nome.count(' ') #pega o total do tamanho de carateres e subtrai com a quantidade de caracteres vazios.
primeiro = nome.find(' ') #Vai dizer em que posição começa o seu primeiro espaço vazio e

print("Analisando seu nome...")
print("Seu nome em letras maiúsculas é {}".format(maiscula))
print("Seu nome em letras minúsculas é {}".format(minuscula))
print("Seu nome tem ao todo {} letras".format(total))
print("Seu primeiro nome tem {} letras".format(primeiro))


