'''
=======================================================================================
MINIPROJETO: PARADIGMA ESTRUTURADO EM PYTHON
GRUPO: MAÍSA GABRIELE BOM, LUIS GUSTAVO MELO, NATALY V. ANANIAS FERNANDES
AULA: 12
TÍTULO DO SISTEMA: SISTEMA DE CONTROLE DE LIVROS DE UMA BIBLIOTECA
DESCRIÇÃO: Um sistema simples para controlar os livros de uma biblioteca,
permitindo adicionar livros, emprestar livros e visualizar o acervo atual.
Utiliza dicionário para armazenar os livros e suas quantidades,
com validação de entrada para garantir dados corretos.
=======================================================================================
'''

def escreve_acervo(): # função para escrever o acervo atualizado no arquivo dados.txt
    with open("dados.txt", "w", encoding="utf-8") as f:
        for livro, qtd in acervo.items():
            f.write(f"{livro}: {qtd}\n")
        f.flush() # garante que os dados sejam escritos no arquivo antes de fechá-lo
        f.close() # fecha o arquivo para liberar recursos do sistema

# CABEÇALHO DO PROGRAMA #str
print("\n==========================================================")
print("========= SISTEMA DE CONTROLE DE UMA BIBLIOTECA ==========")
print("==========================================================")

# LISTA DE LIVROS #str
acervo = {
    "Dom Casmurro": 5,
    "O Pequeno Príncipe": 3,
    "Harry Potter": 10,
    "Senhor dos Anéis": 0,
}

# função para validar nome
def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip()

        if nome == "":
            print("Nome não pode ser vazio!")
        elif not all(c.isalpha() or c.isspace() or c in "'ãõáéíóúâêôç" for c in nome.lower()):
            print("Digite apenas letras!")
        else:
            return nome

# função para validar número
def ler_numero(mensagem):
    while True: # bool parcial
        valor = input(mensagem)

        if not valor.isdigit():
            print("Digite apenas números!")
        else:
            return int(valor)

# função para adicionar livros
def adicionar_livro(nome, quantidade):
    if nome in acervo:
        acervo[nome] += quantidade
    else:
        acervo[nome] = quantidade
    print(f"{quantidade} unidades de '{nome}' adicionadas ao acervo.")
    escreve_acervo()

# função para emprestar livros
def emprestar_livro(nome, quantidade):
    if nome in acervo and acervo[nome] >= quantidade:
        acervo[nome] -= quantidade
        print(f"Empréstimo realizado: {quantidade} unidades de '{nome}'")
    elif nome in acervo and acervo[nome] < quantidade:
        print("Quantidade insuficiente no acervo!")
    else:
        print("Livro não encontrado!")
    escreve_acervo()

# MENU
while True: # bool parcial
    print("\n=================== ESCOLHA UMA OPÇÃO: ===================")
    print("1 - Ver acervo")
    print("2 - Emprestar livro")
    print("3 - Adicionar livro")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":  # VER ACERVO
        print("===================== VER ACERVO =====================")
        print("\nAcervo atual:")
        for livro, qtd in acervo.items():
            status = "Disponível" if qtd > 0 else "Indisponível"
            print(f"{livro}: {qtd} - {status}")

    elif opcao == "2":  # EMPRESTAR LIVRO
        print("=================== EMPRESTAR LIVRO ====================")
        nome = ler_nome("Nome do livro: ")
        qtd = ler_numero("Quantidade: ")
        emprestar_livro(nome, qtd)

    elif opcao == "3":  # ADICIONAR LIVRO
        print("=================== ADICIONAR LIVRO ====================")
        nome = ler_nome("Nome do livro: ")
        qtd = ler_numero("Quantidade: ")
        adicionar_livro(nome, qtd)

    elif opcao == "0":
        print("==========================================================")
        print("================= SISTEMA ENCERRADO ======================")
        print("==========================================================")
        break

    else:
        print("Opção inválida!")

# FIM DO SISTEMA