# ===================================================================
# SISTEMA DE APROVAÇÃO DE ALUNOS
# ===================================================================
# DISCIPLINA : Programação de Sistemas (PS)
# AULA       : 04 - Atividade de desafio
# NOME       : Maísa Gabriele Bom
# DATA       : 15/03/2026
# ===================================================================
# REPOSITÓRIO: https://github.com/20251ctb0100037-code/2026-PS      
# ===================================================================
# DESCRIÇÃO  :
# Este sistema mostra cadastros, empréstimos, catálogos de livros de uma biblioteca, etc
# ===================================================================
# CONCEITOS  : estruturas de dados, listas e dicionários
# ===================================================================

# catálogo inicial
catalogo = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "disponivel": True},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "disponivel": False},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "ano": 1943, "disponivel": True}
]

print("CATALOGO DE LIVROS\n")

# mostrar livros
for livro in catalogo:
    if livro["disponivel"]:
        status = "Disponivel"
    else:
        status = "Emprestado"

    print(livro["titulo"], "-", livro["autor"], "-", status)

# cadastrar novo livro
print("\nCadastrar novo livro")

titulo = input("Titulo: ")
autor = input("Autor: ")
ano = int(input("Ano: "))

novo = {
    "titulo": titulo,
    "autor": autor,
    "ano": ano,
    "disponivel": True
}

catalogo.append(novo)

print("\nCatalogo atualizado:\n")

for livro in catalogo:
    if livro["disponivel"]:
        status = "Disponivel"
    else:
        status = "Emprestado"

    print(livro["titulo"], "-", livro["autor"], "-", status)

# busca por autor
print("\nBuscar por autor")
busca = input("Digite o nome do autor: ").lower()

achou = False

for livro in catalogo:
    if busca in livro["autor"].lower():
        print("Livro encontrado:", livro["titulo"])
        achou = True

if achou == False:
    print("Nenhum livro encontrado")

# contagem
disponiveis = 0
emprestados = 0

for livro in catalogo:
    if livro["disponivel"]:
        disponiveis = disponiveis + 1
    else:
        emprestados = emprestados + 1

print("\nResumo:")
print("Disponiveis:", disponiveis)
print("Emprestados:", emprestados)