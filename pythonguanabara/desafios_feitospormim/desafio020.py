"""O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

aluno1 = input('Digite o nome do primeiro aluno:')
aluno2 = input('Digite o nome do segundo aluno:')
aluno3 = input('Digite o nome do terceiro aluno:')
aluno4 = input('Digite o nome do quarto aluno:')

aluno = [aluno1, aluno2, aluno3, aluno4]
alunos_ordenados = sorted(aluno)

print('O nome dos quatro alunos escolhidos na ordem sorteada. Foram: {}'.format(alunos_ordenados))
