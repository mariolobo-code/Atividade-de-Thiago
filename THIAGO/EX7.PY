# Solicitando o peso e a altura do usuário
peso = float(input("Digite o seu peso em kg (ex: 70.5): "))
altura = float(input("Digite a sua altura em metros (ex: 1.75): "))

# Calculando o IMC (peso dividido pela altura ao quadrado)
imc = peso / (altura ** 2)

# Exibindo o valor do IMC com duas casas decimais
print(f"Seu IMC é: {imc:.2f}")

# Classificando o IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Normal")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")