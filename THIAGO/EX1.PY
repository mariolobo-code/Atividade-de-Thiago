# Solicita a nota do aluno
nota = float(input("Digite a nota do aluno: "))

# Verifica a situação do aluno
if nota >= 7.0:
    print("Situação: Aprovado")
elif nota >= 5.0:
    print("Situação: Em recuperação")
else:
    print("Situação: Reprovado")


 