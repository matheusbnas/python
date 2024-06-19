#Nota do aluno
nota_p1 = float(input("Nota da P1: "))
nota_p2 = float(input("Nota da P2: "))
nota_p3 = float(input("Nota da P3: "))
nota_p4 = float(input("Nota da P4: "))

media = float(6.0)

nota = (nota_p1 + nota_p2 + nota_p3 + nota_p4) / 4

if nota < media:
    print(f"nota {nota}. Precisa fazer prova de recuperação.")
else:
    print(f"Aprovado com média {nota}")