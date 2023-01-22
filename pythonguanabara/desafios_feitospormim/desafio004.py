#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ') #todo input retorna como um tipo primitivo str(string)
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())  #A letra a é um objeto todo objeto tem características que realiza funcionalidade. Eles tem atributos e métodos.
print('É  um número? ',a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanúmerico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizado?', a.istitle())

