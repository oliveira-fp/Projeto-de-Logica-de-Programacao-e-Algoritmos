# Sistema de Pedidos para Fábrica de Camisetas
def escolha_modelo():
    """
    Função para seleção do modelo de camiseta e retorno do valor unitário
    """
    while True:
        # Exibe as opções de modelos disponíveis
        print('''
Entre com o modelo desejado
MCS - Manga Curta Simples
MLS - Manga Longa Simples
MCE - Manga Curta com Estampa
MLE - Manga Longa com Estampa''')

        # Recebe e converte a entrada para maiúsculas
        modelo = input('>>').upper()

        # Define o preço conforme o modelo selecionado
        if modelo == "MCS":
            valorModelo = 1.80
        elif modelo == "MLS":
            valorModelo = 2.10
        elif modelo == "MCE":
            valorModelo = 2.90
        elif modelo == "MLE":
            valorModelo = 3.20
        else:
            print('Escolha inválida, entre com o modelo novamente\n')
            continue
        return valorModelo

def num_camisetas():
    """
    Função para receber a quantidade de camisetas e calcular descontos por volume
    Retorna a quantidade com desconto aplicado
    """
    desconto = 0
    while True:
        try:
            # Tenta converter a entrada para inteiro
            quantidadeCamisetas = int(input('Entre com o número de camisetas: '))
        except ValueError:
            # Tratamento para entradas não numéricas
            print('Por favor, entre com o número de camisetas novamente.\n')
            continue
        else:
            # Verifica se a quantidade não excede o limite máximo
            if quantidadeCamisetas > 20000:
                print('Não aceitamos tantas camisetas de uma vez.')
                print('Por favor, entre com o número de camisetas novamente.\n')
                continue

            # Define a porcentagem de desconto conforme a quantidade
            if quantidadeCamisetas < 20:
                desconto = 0
            elif 20 <= quantidadeCamisetas < 200:
                desconto = 0.05
            elif 200 <= quantidadeCamisetas < 2000:
                desconto = 0.07
            else:
                desconto = 0.12

            # Aplica o desconto na quantidade (economia de escala)
            quantidadeCamisetas -= quantidadeCamisetas * desconto
            return quantidadeCamisetas

def frete():
    """
    Função para seleção da opção de frete e retorno do valor
    """
    while True:
        # Exibe as opções de frete disponíveis
        print('''
Escolha o tipo de frete:
1 - Frete por transportadora - R$ 100.00
2 - Frete por Sedex - R$ 200.00
0 - Retirar pedido na fábrica - R$ 0.00''')
        frete = input('>>')

        # Define o valor do frete conforme a opção selecionada
        if frete == '1':
            valorFrete = 100.00
        elif frete == '2':
            valorFrete = 200.00
        elif frete == '0':
            valorFrete = 0.0
        else:
            print('Opção inválida, tente novamente')
            continue
        return valorFrete

def main():
    """
    Função principal que direciona todo o fluxo do programa
    """
    print('Bem-vindo a Fábrica de Camisetas')

    # Obtém as informações do pedido
    modelo = escolha_modelo()
    quantidade = num_camisetas()
    valorFrete = frete()

    # Calcula o valor total do pedido
    totalPagar = modelo * quantidade + valorFrete

    # Exibe o resumo detalhado do pedido
    print(f"Total: R$ {totalPagar:.2f} (Modelo: {modelo:.2f} * Quantidade(com desconto): {quantidade:.0f} + frete: {valorFrete:.2f})")

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
