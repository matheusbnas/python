"""Crie um programa que leia o nome de uma cidade
e diga se ela começa com o nome 'Santo'"""


cid = str(input("Em que cidade você nasceu? ")).strip()
print(cid[0:5].upper() == 'SANTO')

