"""O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

import random
aluno1 = input('Digite o nome do primeiro aluno:')
aluno2 = input('Digite o nome do segundo aluno:')
aluno3 = input('Digite o nome do terceiro aluno:')
aluno4 = input('Digite o nome do quarto aluno:')

aluno = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(aluno)  #shuffle significa embaralhar e random de aleatório

print('A ordem de apresentação será ')
print(aluno)