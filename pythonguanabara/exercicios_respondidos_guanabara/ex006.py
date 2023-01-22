#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

print('O dobro de {} é {}'.format(n,(n*2)))
print('O triplo de {} é {}.\nA raiz quadrada de {} é {}'.format(n, (n*3), n, (n**(1/2)))) #também funciona com pow(n,(1/2))