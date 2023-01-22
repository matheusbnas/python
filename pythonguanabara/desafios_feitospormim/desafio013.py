#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo novo salário, com 15% de aumento.

salario = float(input('Qual o salário do funcionário?'))

aumento = salario + (salario*15/100)

print('Um funcionário que ganhava R${}, com 15% de aumento, passa a ganhar R${}'.format(salario,aumento))