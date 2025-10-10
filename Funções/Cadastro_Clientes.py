def Cadastro_Clientes():
    print("Cadastro de Clientes")  # Exibe o título do cadastro
    nome = input("Digite o nome do cliente: ")  # Solicita o nome do cliente
    email = input("Digite o email do cliente: ")  # Solicita o email do cliente
    Rua = input("Digite a rua do cliente: ")  # Solicita a rua
    Numero = input("Digite o número do cliente: ")  # Solicita o número
    Bairro = input("Digite o bairro do cliente: ")  # Solicita o bairro
    Cidade = input("Digite a cidade do cliente: ")  # Solicita a cidade
    Estado = input("Digite o estado do cliente: ")  # Solicita o estado
    cliente = {
        "nome": nome,      # Armazena o nome
        "email": email,    # Armazena o email
        "Rua": Rua,        # Armazena a rua
        "Numero": Numero,  # Armazena o número
        "Bairro": Bairro,  # Armazena o bairro
        "Cidade": Cidade,  # Armazena a cidade
        "Estado": Estado,  # Armazena o estado
    }
    print("Cliente cadastrado com sucesso!")  # Mensagem de confirmação
    print(cliente)  # Exibe os dados do cliente
    salvar_cliente(cliente)  # Chama a função para salvar o cliente no JSON

def salvar_cliente(cliente, nome_arquivo="clientes.json"):
    import json  # Importa o módulo json
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            clientes = json.load(f)  # Tenta carregar clientes já existentes
    except FileNotFoundError:
        clientes = []  # Se não existir, cria lista vazia
    clientes.append(cliente)  # Adiciona o novo cliente à lista
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(clientes, f, ensure_ascii=False, indent=4)  # Salva todos os clientes no arquivo
    print(f"Cliente salvo em {nome_arquivo}.")  # Mensagem de confirmação
