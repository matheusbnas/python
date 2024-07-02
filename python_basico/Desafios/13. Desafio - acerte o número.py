# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#   - se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

def adivinha_numero():
    numero_secreto = 14
    tentativas = 0

    while  tentativas < 3:
        num = int(input("Entre com um número: "))
        tentativas += 1

        if num < numero_secreto:
            print('Mais alto')
            print()
        elif num > numero_secreto:
            print('Mais baixo')
            print()
        else:
            print(f"Acertou o numero correto que é {num}")

    if tentativas > 3:
        print("Você não acertou o número secreto.")

adivinha_numero()
