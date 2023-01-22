#crie um script Python que leia o nome dae uma pessoa e mostra uma mensagem de boas-vindas de acordo com o valor digitado.


nome = input('Qual é o seu nome? ')

print('Olá',nome,'! Prazer em te conhecer!')
print('Olá {} ! Prazer em te conhecer!'.format(nome))