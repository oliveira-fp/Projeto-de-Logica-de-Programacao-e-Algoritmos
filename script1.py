# Sistema de Parcelamento de Compras da loja
print("Bem-vindo a Loja")

# Solicita ao usuário o valor total do pedido e a quantidade de parcelas
valorDoPedido = float(input("Entre com o valor do pedido: "))
quantidadeParcelas = int(input("Entre com a quantidade de parcelas: "))

# Define a taxa de juros com base na quantidade de parcelas:
# - Até 3 parcelas: sem juros (0%)
# - 4-5 parcelas: 4% de juros
# - 6-8 parcelas: 8% de juros
# - 9-12 parcelas: 16% de juros
# - 13 ou mais parcelas: 32% de juros
if quantidadeParcelas < 4:
    juros = 0
elif 4 <= quantidadeParcelas < 6:
    juros = 0.04
elif 6 <= quantidadeParcelas < 9:
    juros = 0.08
elif 9 <= quantidadeParcelas < 13:
    juros = 0.16
else:
    juros = 0.32

# Calcula o valor de cada parcela com juros aplicados
# Fórmula: (valor total + juros) / número de parcelas
# Calcula o valor total do pedido com juros
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

# Exibe os resultados formatados com 2 casas decimais
print(f"O valor das parcelas é de: R$ {valorDaParcela:.2f}")
print(f"O valor Total Parcelado é de: R$ {valorTotalParcelado:.2f}")

