"""Um professor quer sortear um dos seus quatro alunos para
apagar o quadro. Faça um programa que ajude ele, lendo o nome
delas e escrevendo o nome do escolhido."""

import random

aluno1 = input('Digite o nome do primeiro aluno que serão sorteados: ')
aluno2 = input('Digite o nome do segundo aluno que serão sorteados: ')
aluno3 = input('Digite o nome do terceiro aluno que serão sorteados:')
aluno4 = input('Digite o nome do quarto aluno que serão sorteados:')

aluno = [aluno1,aluno2,aluno3,aluno4]
sorteado = random.choices(aluno)

print('O nome do aluno escolhido foi: {}'.format(sorteado))