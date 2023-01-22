#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um número: '))

dob = n * 2
trip = n * 3
raiz = n**(1/2)

print('O dobro {} é {}, o triplo de {} é {} e a raiz quadrada de {} é {}'.format(n,dob,n,trip,n,raiz))

