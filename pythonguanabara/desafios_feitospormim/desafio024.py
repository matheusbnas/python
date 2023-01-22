"""Crie um programa que leia o nome de uma cidade
e diga se ela começa com o nome 'Santo'"""


cidade = str(input("Em que cidade você nasceu? ")).strip()

cid = ("Santo")
c = cidade.capitalize()

print(c[0:5] == cid)

