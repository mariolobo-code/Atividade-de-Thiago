# Valores pré-definidos para o usuário e a senha
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "12345"

# Solicitando a entrada do usuário
usuario_digitado = input("Digite o nome de usuário: ")
senha_digitada = input("Digite a senha: ")

# Verificando se os valores conferem
if usuario_digitado == USUARIO_CORRETO and senha_digitada == SENHA_CORRETA:
    print("Login bem-sucedido")
else:
    print("Usuário ou senha inválidos")# Solicitando a entrada do usuário
usuario_digitado = input("Digite o nome de usuário:")
senha_digitada = input("Digite a senha: ")

# Verificando se os valores conferem