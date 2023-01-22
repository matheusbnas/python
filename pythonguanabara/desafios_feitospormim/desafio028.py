"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
 usuário tentar descobrir qual foi o número escolhido pelo computador

 O programa deverá escrever na tela se o usuário venceu ou perdeu"""
print("####### Jogo da adivinhação ######")

import random
num = int(input("Qual número eu pensei?"))

computador = random.randint(0,5) #criar uma aleotoridade por meio do random, n intervalo de 0 a 5 por meio do randint

if num == computador:
    print("Você acertou o número do computador!")
else:
    print("Você errou otário!")
