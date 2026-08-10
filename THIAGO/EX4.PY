# Solicita o valor da compra
valor = float(input("Digite o valor da compra: R$ "))

# Aplica o desconto conforme a regra
if valor >= 200:
    percentual = 0.20
    texto_percentual = "20%"
elif valor >= 100:
    percentual = 0.10
    texto_percentual = "10%"
else:
    percentual = 0.05
    texto_percentual = "5%"

# Cálculos
valor_desconto = valor * percentual
valor_final = valor - valor_desconto

# Exibe os resultados
print(f"\nDesconto aplicado: {texto_percentual}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")