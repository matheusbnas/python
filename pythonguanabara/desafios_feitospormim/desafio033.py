"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor"""

num = str(input("Digite três números: ").strip())

num = num.split()

print(num)
print("##############MAIOR E MENOR################")

if num[0] > num[1] > num[2]:
    print('O maior número é: ', num[0])
    print('O menor número é: ', num[2])
elif num[0] > num[2] > num[1]:
    print('O maior número é: ', num[0])
    print('O menor número é: ', num[1])
elif num[1] > num[0] > num[2]:
    print('O maior número é:', num[1])
    print('O menor número é: ', num[2])
elif num[1] > num[2] > num[0]:
    print('O maior número é: ', num[1])
    print('O menor número é ', num[0])
elif num[2] > num[1] > num[0]:
    print('O maior número é: ', num[2])
    print('O menor número é: ', num[0])
elif num[2] > num[0] > num[1]:
    print('O maior número é: ', num[2])
    print('O menor número é: ', num[1])
elif num[0] == num[1] > num[2]:
    print('O maior número é: ', num[0])
    print('O menor número é: ', num[2])
elif num[0] == num[2] > num[1]:
    print('O maior número é: ', num[0])
    print('O menor número é: ', num[1])
elif num[1] == num[2] > num[0]:
    print('O maior número é: ', num[1])
    print('O menor número é: ', num[0])
else:
    print('Todos os números são iguais')
#elif num[0] == num[1] == num[2]:
#   print('Todos os números são iguais')

