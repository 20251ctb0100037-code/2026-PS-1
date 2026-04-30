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

def escreve_acervo(): # função para escrever o acervo atualizado no arquivo arquivo.txt
    with open("arquivo.txt", "w", encoding="utf-8") as f:
        for livro, qtd in acervo.items():
            f.write(f"{livro}: {qtd}\n") # escreve cada livro e sua quantidade no arquivo

# CABEÇALHO DO PROGRAMA
print("==========================================================") #str para exibir o cabeçalho do sistema
print("=== SISTEMA DE CONTROLE DE UMA BIBLIOTECA ===")
print("==========================================================")

# --- LISTA DE LIVROS ---
acervo = {
    "Dom Casmurro": 5, # dicionário para armazenar a quantidade dos livros da biblioteca #str 
    "O Pequeno Príncipe": 3,
    "Harry Potter": 10,
    "Senhor dos Anéis": 0,
}

# função para validar nome (somente letras)
def ler_nome(mensagem):
    while True: # loop para garantir que o nome seja válido
        nome = input(mensagem).strip()

        if nome == "":
            print("Nome não pode ser vazio!")
        elif not all(c.isalpha() or c.isspace() or c in "'ãõáéíóúâêôç" for c in nome.lower()): 
            print("Digite apenas letras!") # str para exibir a mensagem de erro caso o nome contenha caracteres inválidos
        else:
            return nome

# função para validar número
def ler_numero(mensagem):
    while True: # loop para garantir que o valor seja um número válido
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
    print(f"{quantidade} unidades de '{nome}' adicionadas ao acervo.") # str para exibir a mensagem de confirmação da adição do livro ao acervo
    escreve_acervo()

# função para emprestar livros
def emprestar_livro(nome, quantidade):
    if nome in acervo and acervo[nome] >= quantidade: # verifica se o livro existe e se há quantidade suficiente para emprestar
        acervo[nome] -= quantidade 
        print(f"Empréstimo realizado: {quantidade} unidades de '{nome}'")
    elif nome in acervo and acervo[nome] < quantidade: 
        print("Quantidade insuficiente no acervo!")
    else:
        print("Livro não encontrado!")
    escreve_acervo()

# cabeçalho do projeto (pagina incial)
# MENU (permite escolha de opções)
while True: # loop para exibir o menu até que o usuário escolha sair
    print("=================== ESCOLHA UMA OPÇÃO: ===================")
    print("\n1 - Adicionar livro")
    print("2 - Emprestar livro")
    print("3 - Ver acervo")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1": # exibe o menu para adicionar um livro ao acervo
        print("=================== ADICIONAR LIVRO ====================")
        nome = ler_nome("Nome do livro: ")
        qtd = ler_numero("Quantidade: ")
        adicionar_livro(nome, qtd)

    elif opcao == "2": # exibe o menu para emprestar um livro (diminui a quantidade do acervo)
        print("=================== EMPRESTAR LIVRO ====================")
        nome = ler_nome("Nome do livro: ")
        qtd = ler_numero("Quantidade: ")
        emprestar_livro(nome, qtd)

    elif opcao == "3": # exibe o acervo atual da biblioteca, mostrando a quantidade de cada livro e se está disponível ou não
        print("===================== VER ACERVO =====================")
        print("\nAcervo atual:")
        for livro, qtd in acervo.items():
            status = "Disponível" if qtd > 0 else "Indisponível"
            print(f"{livro}: {qtd} - {status}")

    elif opcao == "0": # exibe a mensagem de encerramento do sistema e sai do loop
        print("==========================================================")
        print("================ SISTEMA ENCERRADO ======================")
        print("==========================================================")
        break

    else:
        try: # TRY EXCEPT caso o usuário digite uma opção inválida, exibe a mensagem de erro e continua o loop
            raise Exception("Opção inválida!")
        except Exception as e:
            print(e)

# FIM DO SISTEMA