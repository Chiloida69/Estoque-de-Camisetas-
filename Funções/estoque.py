import CadastroCamisa

def estoque():
    table_camisas = CadastroCamisa.carregar_camisas()  # Carrega as camisas existentes
    total_estoque = sum(detalhes.get('Quantidade', 0) for detalhes in table_camisas.values())

    print(f"\n--- Relatório de Estoque ---")
    print(f"Total de camisas em estoque: {total_estoque}\n")

    if not table_camisas:
        print("O estoque está vazio.")
        return

    print("Detalhes do estoque:")
    # Cabeçalho com "Time" antes de "Modelo"
    print("-----------------------------------------------------------------------------------------------------------------")
    print(f"{'Time':<20}{'Modelo':<20}{'Marca':<15}{'Cor':<15}{'Tamanho':<10}{'Quantidade':>10}")
    print("-----------------------------------------------------------------------------------------------------------------")

    # Itera sobre as camisas para imprimir os detalhes
    for modelo, detalhes in table_camisas.items():
        # Usa .get() com um valor padrão para evitar erros caso algum campo esteja faltando
        marca = detalhes.get('Marca', 'N/A')
        time = detalhes.get('Time', 'N/A')
        cor = detalhes.get('Cor', 'N/A')
        tamanho = detalhes.get('Tamanho', 'N/A')
        quantidade = detalhes.get('Quantidade', 0)

        # Detalhes com "time" antes de "modelo"
        print(f"{time:<20}{modelo:<20}{marca:<15}{cor:<15}{tamanho:<10}{quantidade:>10}")

    print("-----------------------------------------------------------------------------------------------------------------")
#estoque()