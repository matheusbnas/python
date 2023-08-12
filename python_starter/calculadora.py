#importar bibliotecas
import os

#Entrada dos números
num1 = float(input('Entre com um número: '))
num2 = float(input('Entre com um número: '))
operacao = {
         0 : 'soma', 
         1 : 'subtracao', 
         2 : 'multiplicacao', 
         3 : 'divisao',
         4 : 'exponenciacao',
        }

while True:
    os.system("clear")
    print("-" * 50)
    print("Operação\t\tIndice")
    print("-" * 50)
    for chave, valor in operacao.items():
        print(f'{chave:<20}\t{valor:<20}')
    chave = input("Insira o código da operação (0, 1, 2, 3 ou 4): ")
    chave_lista = list(operacao.keys())
    
    if chave == '0':
        soma = num1 + num2
        print(f'A soma é {soma}')
    elif chave == '1':
        subtracao = num1 - num2
        print(f'A subtração é {subtracao}')
    elif chave == '2':
        multiplicacao = num1 * num2
        print(f'A multiplicação é {multiplicacao}')
    elif chave == '3':
        divisao = num1 / num2
        print(f'A divisão é {divisao}')
    elif chave == '4':
        exponenciacao = num1 ** num2
        print(f'A exponenciação é {exponenciacao}')
    
    choice = input('Deseja continuar fazendo operações matemáticas? (S/N): ').upper()
    num1 = float(input('Entre com um número: '))
    num2 = float(input('Entre com um número: '))
    if choice == "N":
        print("Finalizando as operações...")
        break
    elif choice != "S":
        print("Opção inválida!")
        break