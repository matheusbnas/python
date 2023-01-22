"""Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7,00 por cada Km acima do limite"""


velocimetro = float(input('Velocidade do carro marcado no radar: ')) #primeiro faz a entrada do número

diferenca = velocimetro - 80 # Depois coloca as variáveis
multa = 7 * diferenca
if velocimetro > 80: #Depois vem as condições  (se ou se não)
    print("O motorista foi multado por passar o limite de velocidade permitido: R${:0.2f} de multa".format(multa))
else:
    print("O motorista não foi multado")
