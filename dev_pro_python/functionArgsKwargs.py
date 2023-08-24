def f(*args): #Só aceita parâmetros passados por string(nomeados)
    print(args)
    print(type(args))

f()
print()
f(nome='Matheus')
print()
f(nome = 'Matheus', sobrenome = 'Bernardes')
print()
args = (3,4,5,3)
kwargs = {'nome': 'Matheus', 'sobrenome': 'Bernardes'}
def f(*args, **kwargs):
    print(args)
    print(kwargs)

f(1,2, nome = 'Matheus', sobrenome = 'Bernardes') 
f(args, kwargs)
f(*args, **kwargs)