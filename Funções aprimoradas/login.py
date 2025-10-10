import usuarios_db

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
        return True
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
        return False