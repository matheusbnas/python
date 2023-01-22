"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo."""


print('Analisando triângulos')
print('+=+=+=+=+=+=+=+=+=+=+=+=+=+')
a = float(input('Primeiro segmento:'))
b = float(input('Segundo segmento:'))
c = float(input('Terceiro segmento:'))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM FORMAR triângulos!')
else:
    print('Os segmentos NÃO PODEM FORMAR triângulos')