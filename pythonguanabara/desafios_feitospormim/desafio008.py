#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e melímetros

n = int(input('Entre com um valor: '))

c = n * 100
m = n * 1000

print("O valor em metros é {} metros".format(n))
print('O valor convertido em centímetros e milímetros é : {} centímetros e {} milímetros'.format(c,m))