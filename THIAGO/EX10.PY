# Solicitando a temperatura em graus Celsius
temperatura = float(input("Digite a temperatura em graus Celsius: "))

# Classificando a temperatura com base nos critérios
if temperatura >= 30:
    print("Muito quente")
elif 20 <= temperatura < 30:
    print("Agradável")
elif 10 <= temperatura < 20:
    print("Fresco")
else:
    print("Frio (abaixo de 10°C)")
    