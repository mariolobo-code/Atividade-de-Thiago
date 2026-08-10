# Solicitando o ano ao usuário
ano = int(input("Digite um ano: "))

# Verificando as regras do ano bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")