# Sistema de Pedidos para Loja de Marmitas
# Exibe o cabeçalho e cardápio
print("------------------ Bem-vindo a Loja de marmitas------------------")
print('''-------------------------------Cardápio--------------------------
-----------------------------------------------------------------
---|  Tamanho  |  Bife Acebolado(BA)  |  Filé de Frango(FF)  |---
---|     P     |       R$ 16,00       |       R$ 15,00       |---
---|     M     |       R$ 18,00       |       R$ 17,00       |---
---|     G     |       R$ 22,00       |       R$ 21,00       |---
-----------------------------------------------------------------''')

# Inicializa o valor total do pedido
valorTotal = 0

# Loop principal para múltiplos pedidos
while True:
    # Validação do sabor e tamanho
    while True:
        sabor = input("Entre com o sabor desejado (BA/FF): ").upper()
        if sabor in ["BA", "FF"]:
            tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()
            if tamanho in ["P", "M", "G"]:
                break  # Sai do loop de validação se ambos estiverem corretos
            else:
                print("Tamanho inválido. Tente novamente\n")
                continue
        else:
            print("Sabor inválido. Tente novamente\n")
            continue

    # Define o preço com base no sabor e tamanho
    if sabor == "BA":
        pedido = "Bife Acebolado"
        if tamanho == "P":
            preco = 16.00
        elif tamanho == "M":
            preco = 18.00
        else:
            preco = 22.00
    elif sabor == "FF":
        pedido = "Filé de Frango"
        if tamanho == "P":
            preco = 15.00
        elif tamanho == "M":
            preco = 17.00
        else:
            preco = 21.00

    # Exibe o resumo do item pedido
    print(f"Você pediu um {pedido} no tamanho {tamanho}: R$ {preco:.2f}\n")

    # Atualiza o valor total do pedido
    valorTotal += preco

    # Verifica se o cliente deseja adicionar mais itens
    continuar = input("Deseja mais alguma coisa? (S/N): ").upper()
    if continuar == "N":
        # Exibe o valor total e encerra o programa
        print(f"\nO valor total a ser pago: R$ {valorTotal:.2f}\n")
        break
