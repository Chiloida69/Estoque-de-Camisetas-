import json
import CadastroCamisa
import CadastroEquipe
# Função para pesquisar camisas por um termo específico
def pesquisa():
    # Exibe o título do menu de pesquisa
    print("--- Menu de Pesquisa ---")
    # Exibe as opções de pesquisa disponíveis
    print("1 - Pesquisar por modelo")
    print("2 - Pesquisar por cor")
    print("3 - Pesquisar por tamanho")
    print("4 - Pesquisar por código")
    print("5 - Pesquisar por múltiplos requisitos")
    print("0 - Sair")
    # Inicia um loop para manter o menu ativo até o usuário decidir sair
    while True:
        # Solicita ao usuário que escolha uma opção do menu
        opcao = input("Escolha uma opção: ")
        
        # Pesquisa por modelo
        if opcao == '1':
            termo = input("Digite o modelo: ")  # Recebe o termo de pesquisa
            table_camisas = CadastroCamisa.carregar_camisas()   # Chama a função que retorna o dicionário de camisas cadastradas
            # Chamada CORRETA para a função de pesquisa
            CadastroCamisa.pesquisar_camisas(table_camisas, termo, campo='Modelo')  
            
        # Pesquisa por cor
        elif opcao == '2':
            termo = input("Digite a cor: ")  # Recebe o termo de pesquisa
            table_camisas = CadastroCamisa.carregar_camisas()  # Chama a função que retorna o dicionário de camisas cadastradas
            # Chamada CORRETA para a função de pesquisa
            CadastroCamisa.pesquisar_camisas(table_camisas, termo, campo='Cor')
            
        # Pesquisa por tamanho
        elif opcao == '3':
            termo = input("Digite o tamanho: ")  # Recebe o termo de pesquisa
            table_camisas = CadastroCamisa.carregar_camisas()  # Chama a função que retorna o dicionário de camisas cadastradas
            # Chamada CORRETA para a função de pesquisa
            CadastroCamisa.pesquisar_camisas(table_camisas, termo, campo='Tamanho')
        # Pesquisa por código
        elif opcao == '4':
            termo = input("Digite o código: ")  # Recebe o termo de pesquisa
            table_camisas = CadastroCamisa.carregar_camisas()  # Chama a função que retorna o dicionário de camisas cadastradas
            # Chamada CORRETA para a função de pesquisa
            CadastroCamisa.pesquisar_camisas(table_camisas, termo, campo='Codigo')
        # Pesquisa por múltiplos requisitos
        # Pesquisa por múltiplos requisitos (OPÇÃO 7 - FILTRO COMPLETO)
        elif opcao == '5':
            modelo = input("Modelo (ou Enter para ignorar): ")
            cor = input("Cor (ou Enter para ignorar): ")
            tamanho = input("Tamanho (ou Enter para ignorar): ")
            codigo = input("Código (ou Enter para ignorar): ")
            quantidade = input("Quantidade (ou Enter para ignorar): ") # NOVO INPUT: Quantidade
            
            table_camisas = CadastroCamisa.carregar_camisas()
            resultados = []
            
            for modelo_camisa, detalhes in table_camisas.items():
                
                # 1. Verifica Modelo (Chave Principal)
                if modelo and modelo.strip() and modelo.lower() not in modelo_camisa.lower():
                    continue
                    
                # 2. Verifica Cor
                if cor and cor.strip() and cor.lower() not in detalhes.get('Cor', '').lower(): 
                    continue
                    
                # 3. Verifica Tamanho
                if tamanho and tamanho.strip() and tamanho.lower() not in detalhes.get('Tamanho', '').lower():
                    continue
                        
                # 4. Verifica Código
                if codigo and codigo.strip():
                    codigo_detalhes = str(detalhes.get('Codigo', '')).lower()
                    codigo_busca = codigo.lower()
                    if codigo_busca not in codigo_detalhes:
                        continue
                        
                # 5. Verifica Quantidade (NOVA LÓGICA DE FILTRO)
                if quantidade and quantidade.strip():
                    try:
                        # Converte a busca para int para comparação numérica
                        qtd_busca = int(quantidade)
                        qtd_detalhes = detalhes.get('Quantidade', 0)
                        
                        # Filtra se a quantidade em estoque for menor que o valor mínimo buscado.
                        if qtd_detalhes < qtd_busca:
                            continue
                    except ValueError:
                        print("Aviso: Quantidade deve ser um número inteiro. Filtro de Quantidade ignorado nesta camisa.")
                        # Se o valor não for um número, apenas ignoramos o filtro para esta camisa
                        pass
                    
                # Adiciona ao resultado se todos os filtros passarem
                resultados.append({modelo_camisa: detalhes}) 
                
            if resultados:
                print("\nResultados da pesquisa por múltiplos requisitos:")
                for item in resultados:
                    print(item)
            else:
                print("\nNenhum resultado encontrado para os filtros especificados.")
                
        # ... (continuação do código com elif opcao == '0':)