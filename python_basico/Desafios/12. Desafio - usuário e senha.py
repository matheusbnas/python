# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como
# variávies dentro do próprio código.

def acesso_usuario(usuario_correto,senha_correta):
    if usuario_correto == "matheusbnas" and senha_correta == "123456":
        print("Acesso permitido")
    elif usuario_correto == "matheusbnas" and senha_correta != "123456":
        print("Senha incorreta")
    elif usuario_correto != "matheusbnas" and senha_correta == "123456":
        print("Login incorreto")
    else:
        print("Login e senha incorretos. Não cadastrado")
    
    return None


usuario = input("Escreva seu login: ")
senha = input("Senha: ")
acesso_usuario(usuario, senha)









