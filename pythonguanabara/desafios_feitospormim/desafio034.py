"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%.

Para os salários inferiores ou iguais, o aumento é de 15%."""

salario = float(input("Qual o salário do funcionário? R$"))

#apliquei uma variável global
maior = (salario * 10/100) + salario
menor = (salario * 15/100) + salario

if salario > 1250:
    print("O salário final é: R${:0.2f}".format(maior))
else:
    print("O salário final é: R${:0.2f}".format(menor))