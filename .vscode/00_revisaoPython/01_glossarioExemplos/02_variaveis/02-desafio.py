# ===================================================================
# SISTEMA DE APROVAÇÃO DE ALUNOS
# ===================================================================
# DISCIPLINA : Programação de Sistemas (PS)
# AULA       : 04 - Atividade de desafio
# NOME       : Maísa Gabriele Bom
# DATA       : 24/02/2026
# ===================================================================
# REPOSITÓRIO: https://github.com/20251ctb0100037-code/2026-PS      
# ===================================================================
# DESCRIÇÃO  :
# Este sistema mostra o controle de estoque de uma loja de
# informática.
# ===================================================================
# CONCEITOS  : variáveis, tipos de dados, operadores, estruturas de
# seleção e de repetição.
# ===================================================================
#
print("=== SISTEMA DE CONTROLE DE ESTOQUE ===")
print()
# lista de produtos no estoque
produtos = [
    {"nome": "Notebook", "qtd": 7},
    {"nome": "Teclado", "qtd": 2},
    {"nome": "Pendrive", "qtd": 30}
]

# Conta a situaçao dos estoques
critico = 0
adequado = 0
excesso = 0

print("=== RELATÓRIO DE ESTOQUE ===")

# Laço FOR para ler todos os produtos
for produto in produtos:
    nome = produto["nome"]
    qtd = produto["qtd"]

    # Verifica a situação do estoque
    if qtd < 5:
        situacao = "Crítico"
        critico += 1
    elif qtd <= 20:
        situacao = "Adequado"
        adequado += 1
    else:
        situacao = "Excesso"
        excesso += 1

    # Mostra as informações do produto
    print(f"Produto: {nome} | Quantidade: {qtd} | Situação: {situacao}")

# mostra o estoque em geral
print("\n=== RESUMO DO ESTOQUE ===")
print("Produtos Críticos:", critico)
print("Produtos Adequados:", adequado)
print("Produtos em Excesso:", excesso)

# Laço WHILE para encontrar o produto pelo nome
while True:
    busca = input("\nDigite o nome do produto para consultar (ou 'sair' para encerrar): ")

    if busca.lower() == "sair":
        print("=== PROGRAMA FINALIZADO! ===")
        break

    encontrado = False

    # Busca o produto na lista
    for produto in produtos:
        if produto["nome"].lower() == busca.lower():
            print(f"{produto['nome']} tem {produto['qtd']} unidades em estoque.")
            encontrado = True

    # se o produto for falso
    if not encontrado:
        print("Produto não encontrado na lista! ")