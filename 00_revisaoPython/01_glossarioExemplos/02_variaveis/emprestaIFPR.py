import os #vê se o arquivo usuario.txt já existe no computador.

print("BEM VINDO AO EMPRESTA IFPR!")
print()
print("============================")
print()

arquivo = "usuario.txt"

# pergunta ao usuário
while True:
    print("\n=== ÍNICIO ===")
    print("1 - Login")
    print("2 - Cadastrar")

    opcao = input("Escolha uma opção: ")

    # PRIMEIRO ACESSO automático
    if not os.path.exists(arquivo):
        print("\n=== PRIMEIRO ACESSO ===")
        email = input("Crie seu email: ")
        senha = input("Crie sua senha: ")

# guarda as informaçõe do primeiro login
        with open(arquivo, "w") as f:
            f.write(email + "\n")
            f.write(senha)

        print("Cadastro realizado com sucesso!")
        continue

    # LOGIN
    if opcao == "1":
        print("\n=== LOGIN ===")
        email_digitado = input("Digite seu email: ")
        senha_digitada = input("Digite sua senha: ")

        with open(arquivo, "r") as f:
            email_salvo = f.readline().strip()
            senha_salva = f.readline().strip()

        if email_digitado == email_salvo and senha_digitada == senha_salva:
            print("Login realizado com sucesso!")
        else:
            print("Email ou senha incorretos.")

    # CADASTRAR NOVAMENTE
    elif opcao == "2":
        email = input("Novo email: ")
        senha = input("Nova senha: ")

        with open(arquivo, "w") as f:
            f.write(email + "\n")
            f.write(senha)

        print("Conta atualizada com sucesso!")

