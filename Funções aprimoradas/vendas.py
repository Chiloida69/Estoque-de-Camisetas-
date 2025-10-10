import banco_de_dados

def menu_vendas():
    """
    Função para gerenciar o processo de venda de camisas,
    dando baixa no estoque.
    """
    while True:
        print("--- Menu de Vendas ---")

        # Verifica se o estoque está vazio
        if not banco_de_dados.estoque_camisas:
            print("Nenhuma camisa cadastrada no estoque. Cadastre uma camisa primeiro.")
            break

        # 1. Listar as camisas disponíveis
        print("Camisas em estoque:")
        for modelo, detalhes in banco_de_dados.estoque_camisas.items():
            print(f"-> Modelo: {modelo} | Tamanho: {detalhes['Tamanho']} | Qtd: {detalhes['Quantidade']}")
        
        print('Digite "voltar" a qualquer momento para sair.')
        
        # 2. Pedir para o usuário escolher o modelo
        modelo_venda = input("Digite o nome do MODELO da camisa que deseja vender: ")

        if modelo_venda.lower() == 'voltar':
            print("Voltando ao menu principal...")
            break
        
        # 3. Verificar se a camisa existe no estoque
        if modelo_venda in banco_de_dados.estoque_camisas:
            camisa_selecionada = banco_de_dados.estoque_camisas[modelo_venda]
            estoque_atual = camisa_selecionada['Quantidade']
            
            print(f"Estoque atual da camisa '{modelo_venda}': {estoque_atual} unidades.")
            
            try:
                # 4. Perguntar a quantidade a ser vendida
                qtd_venda = int(input(f"Quantas unidades de '{modelo_venda}' deseja vender? "))

                # 5. Validar o estoque e dar baixa
                if qtd_venda <= 0:
                    print("Quantidade inválida. Por favor, insira um número maior que zero.")
                elif qtd_venda <= estoque_atual:
                    # Se há estoque suficiente, realiza a baixa
                    camisa_selecionada['Quantidade'] -= qtd_venda
                    print(f"Venda realizada com sucesso!")
                    print(f"   Estoque atualizado de '{modelo_venda}': {camisa_selecionada['Quantidade']} unidades.")
                else:
                    # Se não há estoque suficiente, informa o usuário
                    print(f"Estoque insuficiente! Temos apenas {estoque_atual} unidades dessa camisa.")
            
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números para a quantidade.")

        else:
            print(f"Modelo '{modelo_venda}' não encontrado no estoque. Tente novamente.")