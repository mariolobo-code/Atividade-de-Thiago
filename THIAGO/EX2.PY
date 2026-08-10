 #Solicita a idade do usuário
idade = int(input("Digite a idade da pessoa: "))

# Realiza a classificação
if idade <= 11:
    classificacao = "Criança"
elif idade <= 18:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

# Exibe o resultado
print(f"A pessoa é classificada como: {classificacao}")  



