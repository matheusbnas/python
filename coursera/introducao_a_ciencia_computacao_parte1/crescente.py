A=int(input("entre com o primeiro número: "))
B=int(input("entre com o segundo número: "))
C=int(input("entre com o terceiro número: "))

if A < B < C:
    print("crescente")
else:    # poderia ser um elif
    if A > B > C:
        print("não está em ordem crescente")
    else:
        print("não está em ordem crescente")
