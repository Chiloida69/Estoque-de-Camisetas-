def Cadastro_Clientes():
    cliente = carregar_clientes()  # Carrega clientes existentes
    print("Cadastro de Clientes")  # Exibe o título do cadastro
    nome = input("Digite o nome do cliente: ")  # Solicita o nome do cliente
    Chave= input("Digite o CPF/CNPJ do cliente: ")  # Solicita o CPF do cliente
    email = input("Digite o email do cliente: ")  # Solicita o email do cliente
    Rua = input("Digite a rua do cliente: ")  # Solicita a rua
    Numero = input("Digite o número do cliente: ")  # Solicita o número
    Bairro = input("Digite o bairro do cliente: ")  # Solicita o bairro
    Cidade = input("Digite a cidade do cliente: ")  # Solicita a cidade
    Estado = input("Digite o estado do cliente: ")  # Solicita o estado
    cliente = {
        "nome": nome,      # Armazena o nome
        "Chave": Chave,    # Armazena o CPF/CNPJ
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
def carregar_clientes(nome_arquivo="clientes.json"):
    import json  # Importa o módulo json
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)  # Tenta carregar e retornar a lista de clientes
    except FileNotFoundError:
        print("Arquivo não encontrado, retornando lista vazia.")  # Mensagem de erro
        return []  # Retorna lista vazia se o arquivo não existir

def carregar_clientes(nome_arquivo="clientes.json"):
    import json  # Importa o módulo json
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)  # Tenta carregar e retornar a lista de clientes
    except FileNotFoundError:
        print("Arquivo não encontrado, retornando lista vazia.")  # Mensagem de erro
        return []  # Retorna lista vazia se o arquivo não existir

def pesquisar_clientes(termo, campo='nome', nome_arquivo="clientes.json"):
    import json  # Importa o módulo json
    clientes = carregar_clientes(nome_arquivo)  # Carrega a lista de clientes
    resultados = []  # Lista para armazenar resultados da pesquisa
    termo_lower = termo.lower()  # Converte o termo para minúsculas para comparação
    campo_lower = campo.lower()  # Converte o campo para minúsculas para comparação
    for cliente in clientes:
        if campo_lower in cliente and termo_lower in str(cliente[campo_lower]).lower():
            resultados.append(cliente)  # Adiciona cliente aos resultados se corresponder ao termo
    if resultados:
        print(f"\nResultados da pesquisa por '{termo}' no campo '{campo}':")
        for item in resultados:
            print(item)  # Exibe cada cliente encontrado
    else:
        print(f"Nenhum cliente encontrado para '{termo}' no campo '{campo}'.")  # Mensagem se nada for encontrado