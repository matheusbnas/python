#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e melímetros
medida = float(input('Uma medida em metros: '))

cm = medida * 100
mm = medida * 1000

print("O valor em metros é {} metros".format(medida))
print('A medida em {} corresponde a {:.0f} centímetros e {:.0f} milímetros'.format(medida,cm,mm))