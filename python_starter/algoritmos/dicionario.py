TOTAL = 0

products = {
    100: ("Cachorro-quente", 9.00),
    101: ("Cachorro-quente Duplo", 11.00),
    102: ("X-Egg", 12.00),
    103: ("X-Salada", 13.00),
    104: ("X-Bacon", 14.00),
    105: ("X-Tudo", 17.00),
    200: ("Refrigerante Lata", 5.00),
    201: ("Chá Gelado", 4.00),
}

print("-" * 50)
print("Código\t\tNome\t\t\tValor")
print("-" * 50)

for code, (name, price) in products.items():
    print(f"{code}\t\t{name:<25}${price:<25}")

print("-" * 50)

while True:
    order = int(input("Insira o código do produto desejado: "))

    if order in products:
        price = products[order][1]
        TOTAL += price
    else:
        print("Código inválido!")
        continue

    choice = input("Você deseja adicionar mais um produto no pedido? (S/N): ").upper()

    if choice == "N":
        print("Finalizando pedido...")
        break
    elif choice != "S":
        print("Opção inválida!")
        break

print(f"O valor total da compra foi R${TOTAL:.2f}")
print(f"Pedidos: {products[order][0]} - R${products[order][1]:.2f}")