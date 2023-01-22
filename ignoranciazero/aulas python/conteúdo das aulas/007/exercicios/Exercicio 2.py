"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
salario_hora = float(input('Quanto ganha por hora de trabalho: '))
horas_mes =  float(input('Quantas horas você trabalha por mês? '))

total = salario_hora * horas_mes

print('Meu salário no referido mês é: R${:.2f}'.format(total))