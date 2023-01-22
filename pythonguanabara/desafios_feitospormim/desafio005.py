#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('entre com um número: '))

ant = n - 1  # subtração para dizer o antecessor do numero n
suc = n + 1  # soma para dizer o sucessor do numero n

print('O número {} é antecessor do número {} e o número {} é o sucessor'.format(ant,n,suc))