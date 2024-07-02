# Desafio - crie um programa que:
# - Pede pelo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sual idade? "))

print()
print(f"Oi, {nome}!" )
print(f' Quantidade de letras no nome: {len(nome)}')

idade_5 = idade + 5  
print(f'Minha idade daqui a 5 anos: {idade_5}')