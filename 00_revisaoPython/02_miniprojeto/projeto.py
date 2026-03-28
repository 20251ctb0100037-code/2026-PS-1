'''
=======================================================================================
MINIPROJETO: PARADIGMA ESTRUTURADO EM PYTHON
GRUPO: Luis Gustavo Pereira Melo, Maísa Gabriele Bom e Nathaly V. de Ananias Fernandes
AULA: 12
TÍTULO DO SISTEMA: SISTEMA DE ESTOQUE DE UMA PANIFICADORA
DESCRIÇÃO: Um sistema simples para controlar o estoque de uma panificadora, 
que permite adicionar produtos, vender produtos e ver o estoque atual. 
Possui dicionário para armazenar os produtos e as quantidades, 
e inclui validação de entrada para garantir que os dados sejam inseridos corretamente.
=======================================================================================
'''

ARQUIVO = "dados.txt" #onde os dados do estoque serão armazenados em formato de texto

# CABEÇALHO DO PROGRAMA
print("==========================================================")
print("=== SISTEMA DE CONTROLE DO ESTOQUE DE UMA PANIFICADORA ===") 
print("==========================================================")

#---LISTA DOS PRODUTOS DA PANIFICADORA---------
estoque = {    # dicionário para armazenar a quantidade dos produtos da panificadora              
    "Pão de queijo": 7,
    "Pedaço de torta": 2,
    "Sonho de Creme": 30,
    "Bolo de Chocolate": 0,
}

# função para validar nome (somente letras)
def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip() # remove espaços em branco no início e no final do nome

        if nome == "":
            print("Nome não pode ser vazio!")
        elif not all(c.isalpha() or c.isspace() or c in "'ãõáéíóúâêôç" for c in nome.lower()): #Validação para permitir letras acentuadas, espaços e apóstrofos
            print("Digite apenas letras!") #
        else:
            return nome

# função para validar quantidade (somente números)
def ler_numero(mensagem):
    while True:
        valor = input(mensagem)

        if not valor.isdigit(): #Se o valor não for composto apenas por dígitos, exibe msg de erro
            print("Digite apenas números!")
        else:
            return int(valor)

# função para adicionar produtos ao estoque
def adicionar_estoque(nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade # adiciona a quantidade DE um novo produto
    else:
        estoque[nome] = quantidade # adiciona um novo produto ao estoque da panificadora
    print(f"{quantidade} unidades de '{nome}' adicionadas ao estoque.")

# função para vender (remover do estoque)
def vender_produto(nome, quantidade):
    if nome in estoque:
        if estoque[nome] >= quantidade: # ve se a quantidade solicitada para venda é menor ou igual à quantidade disponível no estoque
            estoque[nome] -= quantidade
            print(f"Venda realizada: {quantidade} unidades de '{nome}'") 
        else:
            print("Estoque insuficiente!")
    else:
        print("Produto não encontrado!")

# MENU DE OPÇÕES
# (É aqui que o programa realmente começa)

while True: # loop infinito para exibir o MENU até o usuário escolher sair
    print("=================== ESCOLHA UMA OPÇÃO: ===================")
    print("\n1 - Adicionar produto")
    print("2 - Vender produto")
    print("3 - Ver estoque")
    print("0 - Sair")

    opcao = input("Escolha: ") # LÊ A OPÇÃO ESCOLHIDA DO USUÁRIO

    if opcao == "1": # exibe o menu para adicionar um produto ao estoque
        print("=================== ADICIONAR PRODUTO ====================")
        nome = ler_nome("Nome do produto: ")
        qtd = ler_numero("Quantidade: ")
        adicionar_estoque(nome, qtd)

    elif opcao == "2": # exibe o menu para vender um produto (diminiu o estoque)
        print("===================== VENDER PRODUTO =====================")
        nome = ler_nome("Nome do produto: ")
        qtd = ler_numero("Quantidade: ")
        vender_produto(nome, qtd)

    elif opcao == "3": # exibe o menu para ver o estoque da panificadora
        print("===================== VER ESTOQUE =====================")
        print("\nEstoque atual:")
        for produto, qtd in estoque.items(): # para cada produto e quantidade no estoque, exibe o nome do produto e a quantidade (disponível/indisponível)
            status = "Disponível" if qtd > 0 else "Indisponível"
            print(f"{produto}: {qtd} - {status}")

    elif opcao == "0": # sai do loop infinito, finalizando o programa
        print("==========================================================")
        print("================ SISTEMA ENCERRADO ======================")
        print("==========================================================")
        break

    # FIM DO SISTEMA

    else: # se o usuário digitar uma opção que não seja 1, 2, 3 ou 0
        print("Opção inválida!")
