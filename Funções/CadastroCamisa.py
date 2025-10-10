import json

def CadastroCamisa(): #Define a função para cadastro das camisas.
    TableCamisas = {} #Cria um dicionário vazio para armazenar as camisas cadastradas.
    print("Função de cadastro de camisas chamada.") #Mensagem para indicar que a função foi chamada.
      # Loop para permitir o cadastro de várias camisas
    while True:
        Modelo = input('Cadastre o modelo da camisa (ou digite "sair" para terminar): ')
        # Condição para sair do loop
        if Modelo.lower() == 'sair':
            break #Sai do loop se o usuário digitar 'sair'.
        # Solicita os dados da camisa
        Tamanho = input(f'Cadastre o tamanho da camisa (P, M, G, GG) para o modelo {Modelo}: ')
        Cor = input(f'Cadastre a cor da camisa para o modelo {Modelo}: ')
        try:
            Codigo = int(input(f'Cadastre um código para a camisa {Modelo}: '))
            Quantidade = int(input(f'Cadastre a quantidade de camisas para o modelo {Modelo}: '))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue #Volta para o início do loop para tentar novamente
        # Cria um dicionário com os detalhes da camisa
        detalhes_camisa = {
            'Modelo': Modelo,
            'Tamanho': Tamanho,
            'Cor': Cor,
            'Quantidade': Quantidade,
            'Codigo': Codigo
            
        }
        # Adiciona o novo dicionário ao dicionário principal, usando o modelo como chave
        TableCamisas[Modelo] = detalhes_camisa
        print(f"Camisa '{Modelo}' cadastrada com sucesso!") #Mensagem de confirmação de cadastro.
    print("Cadastro de camisas finalizado.") #Mensagem indicando o fim do cadastro.
    
    # Salva o cadastro ao finalizar
    salvar_camisas(TableCamisas)
    
    return TableCamisas #Retorna o dicionário com as camisas cadastradas.

def salvar_camisas(table_camisas, nome_arquivo="camisas.json"): #SALVA O DICIONÁRIO EM UM ARQUIVO JSON para poder chamalo dps 
    
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(table_camisas, f, ensure_ascii=False, indent=4)
    print(f"Camisas salvas em {nome_arquivo}.")

def carregar_camisas(nome_arquivo="camisas.json"):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado, retornando dicionário vazio.")
        return {}

def pesquisar_camisas(table_camisas, termo, campo='Modelo'):
    """
    Pesquisa camisas na tabela pelo termo em um campo específico.
    Exibe os resultados ou uma mensagem de que nada foi encontrado.
    """
    resultados = []
    termo_lower = termo.lower()
    campo_lower = campo.lower()

    for chave, detalhes in table_camisas.items():
        # Pesquisa pelo Modelo (Chave Principal)
        if campo_lower == 'modelo' and termo_lower in chave.lower():
            resultados.append({chave: detalhes})
        # Pesquisa por campos dentro dos detalhes (Cor, Tamanho, Codigo, etc.)
        elif campo in detalhes:
            valor_campo = str(detalhes[campo]).lower()
            if termo_lower in valor_campo:
                resultados.append({chave: detalhes})

    if resultados:
        print(f"\nResultados da pesquisa por '{termo}' no campo '{campo}':")
        for item in resultados:
            print(item)
    else:
        print(f"\nNenhuma camisa encontrada com '{termo}' no campo '{campo}'.")

    return resultados