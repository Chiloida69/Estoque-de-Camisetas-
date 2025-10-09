def Cadastro_Clientes():# Função para cadastrar clientes
    print("Cadastro de Clientes") # Título do cadastro
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    Rua=input("Digite a rua do cliente: "),
    Numero=input("Digite o número do cliente: "),
    Bairro=input("Digite o bairro do cliente: "),
    Cidade=input("Digite a cidade do cliente: "),   
    Estado=input("Digite o estado do cliente: "), 
    cliente = {
        "nome": nome,
        "email": email,
        "Rua": Rua,
        "Numero": Numero,
        "Bairro": Bairro,
        "Cidade": Cidade,
        "Estado": Estado,   
    }
    
    print("Cliente cadastrado com sucesso!")
    print(cliente)
Cadastro_Clientes() # Chama a função para cadastrar clientes