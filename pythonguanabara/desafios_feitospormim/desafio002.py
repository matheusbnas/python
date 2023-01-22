# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostra uma mensagem com a data formatada.

dia = int(input('Digite o dia em que você nasceu: '))  # número inteiro
mes = input('Digite o mês em que você nasceu: ')       # string
ano = int(input('Digite o ano que você nasceu: '))     # número inteiro


print('Você nasceu no dia {} de {} de {}.'.format(dia,mes,ano))
