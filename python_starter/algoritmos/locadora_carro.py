import os

total = 0
alugados = []

carros = {
    0: ("Chevrolet Tracker", 120),
    1: ("Chevrolet Onix", 90),
    2: ("Chevrolet Spin", 150),
    3: ("Hyundai HB20", 85),
    4: ("Hyundai Tucson", 120),
    5: ("Fiat Uno", 60),
    6: ("Fiat Mobi", 70),
    7: ("Fiat Pulse", 130),
}


def lista_carros(portfolio_carros):
    for codigo, (nome, preco) in portfolio_carros.items():
        print(f"{codigo}\t\t{nome:<25}R${preco:<5}/ dia")


def lista_carros_alugados(cod, del_carro, alugado):
    # Adicionar numa lista e tirar do dicionário!
    alugado.append(del_carro.pop(cod))
    return print(alugado)


def devolver_carro(cod, dev_carro, devolver):
    # Adicionar de volta ao dicionário e tirar da lista!
    devolver.pop(dev_carro.append(cod))
    return print(devolver)


while True:
    # os.system("cls")
    print("Bem vindo à locadora de Carros")
    print("-" * 7)
    print("O que deseja fazer? ")
    print("-" * 7)
    print("0 - Mostrar Portfólio, 1 - Alugar um carro, 2 - Devolver um carro")
    print("-" * 50)
    pedido = int(input("Insira o código desejado: "))
    print()

    # os.system("cls")
    if pedido == 0:
        print("-" * 7)
        print("Código\t\tNome\t\t\tValor")
        print("-" * 7)
        lista_carros(carros)

    elif pedido == 1:
        print("Código\t\tNome\t\t\tValor")
        print("-" * 7)
        lista_carros(carros)
        cod_carro = int(input("Escolha o código do carro de 0 a 7: "))
        dias = int(input("Por quantos dias deseja alugar o carro ? "))
        print()
        # for i in carros.keys():
        if cod_carro not in carros.keys():
            print(f"Código {cod_carro} já selecionado. Tente outro.")
            cod_carro = int(
                input(f"Escolha outro código do carro disponivel: "))
        print(
            f"Código {cod_carro} | Foi escolhido o carro {carros[cod_carro][0]} para {dias} dias.")
        print(
            f"O valor total da compra foi R${(carros[cod_carro][1] * dias):.2f}")
        print()
        # Coloca os carros selecionados numa lista nesta função
        lista_carros_alugados(cod_carro, carros, alugados)

    elif pedido == 2:
        if len(alugados) == 0:

            print("Não tem nenhum carro para devolver!")
            print("Fique a vontade para escolher os carros conforme a lista!")
        else:
            for lista, cod_carro in alugados:
                print(
                    f"Código do carro alugado: {cod_carro} | Carro(os) alugado(s): {alugados}.")
            cod_carro = int(
                input("Escolha o código do carro que deseja devolver: "))

            devolver_carro(cod_carro, carros, alugados)

    else:
        nova_escolha = print(
            "Pedido incorreto. Faça um novo pedido de 0 a 2.\n")

    # continue
    choice = input(
        "Você deseja realizar algum pedido? (S / N): ").upper()

    if choice == "N":
        print()
        print("Finalizando pedido...")
        print("Obrigado pela preferência!")
        break
    elif choice != "S":
        print("Opção inválida! Tente novamente\n")
