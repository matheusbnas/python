#importar bibliotecas
import os

#função calculadora
def calculadora(n1,n2, op):
    if op.values() == 0:
        soma = n1 + n2
    elif op.values() == 1:
        subtracao = n1 - n2
    elif op.values() == 2:
        multiplicacao = n1 * n2
    elif op.values() == 3:
        divisao = n1 / n2
    else:
        print('Deseja continuar fazendo operações matemáticas?')


#Entrada dos números
num1 = float(input('Entre com um número: '))
num2 = float(input('Entre com um número: '))
operacao = input('Qual operação deseja realizar? soma, subtração, multiplicação, divisão: ')
opcao = {'soma' : 0, 'subtracao' : 1, 'multiplicacao' : 2, 'divisao' : 3}
if opcao.keys('soma') == 0:
    soma = num1 + num2
    print(soma)
elif opcao.keys('subtracao') == 1:
    subtracao = num1 - num2
    print(subtracao)
elif opcao.keys('multiplicacao') == 2:
    multiplicacao = num1 * num2
    print(multiplicacao)
elif opcao.keys('divisao') == 3:
    divisao = num1 / num2
    print(divisao)
else:
    print('Deseja continuar fazendo operações matemáticas?')
   # if s == 0:
    #    os.open
    #else:
    #    os.close