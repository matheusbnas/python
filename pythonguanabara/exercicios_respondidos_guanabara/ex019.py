"""Um professor quer sortear um dos seus quatro alunos para
apagar o quadro. Faça um programa que ajude ele, lendo o nome
delas e escrevendo o nome do escolhido."""

import random

n1 = input('Digite o nome do primeiro aluno que serão sorteados: ')
n2 = input('Digite o nome do segundo aluno que serão sorteados: ')
n3 = input('Digite o nome do terceiro aluno que serão sorteados:')
n4 = input('Digite o nome do quarto aluno que serão sorteados:')

aluno = [n1,n2,n3,n4]
sorteado = random.choices(aluno)

print('O nome do aluno escolhido foi: {}'.format(sorteado))