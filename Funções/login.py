import usuarios_db
import menu

def cadastrar_usuario():
    """
    Função para cadastrar um novo usuário.
    """
    print("--- Cadastro de Novo Usuário ---")
    
    while True:
        username = input("Digite o nome de usuário desejado: ")
        
        # Verifica se o usuário já existe
        if username in usuarios_db.usuarios:
            print("Este nome de usuário já existe. Por favor, escolha outro.")
        else:
            break # Sai do loop se o nome de usuário for válido

    password = input(f"Digite a senha para o usuário '{username}': ")
    
    # Adiciona o novo usuário ao dicionário
    usuarios_db.usuarios[username] = password
    print(f"Usuário '{username}' cadastrado com sucesso!")

def fazer_login():
    """
    Função para autenticar um usuário.
    Retorna True se o login for bem-sucedido, False caso contrário.
    """
    print("--- Login ---")
    username = input("Usuário: ")
    password = input("Senha: ")

    # Verifica se o usuário existe e se a senha está correta
    if username in usuarios_db.usuarios and usuarios_db.usuarios[username] == password:
        print(f"Login bem-sucedido! Bem-vindo, {username}.")
        menu.menu_principal()
        return True
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
        return False
    
# Função para o menu de login
def menu_inicial():

    while True:
        print("\n===== BEM-VINDO À LOJA =====")
        print("Você precisa fazer login para continuar.")
        print("1 - Fazer Login")
        print("2 - Cadastrar Novo Usuário")
        print("0 - Sair do Programa")
        
        opcao_login = input("Escolha uma opção: ")

        if opcao_login == '1':
            # Chama a função de login. Se retornar True, o loop é quebrado.
            if fazer_login():
                break
        elif opcao_login == '2':
            cadastrar_usuario()
        elif opcao_login == '0':
            print("Saindo...")
            return
        else:
            print("Opção inválida. Tente novamente.")
menu_inicial()