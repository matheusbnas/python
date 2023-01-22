#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

celsius = float(input('Informe a temperatura em ºC: '))

f = ((9 * celsius) / 5) + 32

print('A temperatura de  {}ºC corresponde a {}ºF'.format(celsius,f))