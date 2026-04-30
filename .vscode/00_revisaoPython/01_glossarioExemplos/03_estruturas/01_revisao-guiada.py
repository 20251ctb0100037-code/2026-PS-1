# ==================================================
# SISTEMA DE BIBLIOTECA
# ==================================================

# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 – Revisão: Estruturas de Dados
# Autor      : [SEU NOME AQUI]
# Data       : [DATA DE HOJE]
# Repositório: https://github.com/20251ctb0100037-code
# ==================================================

#
# DESCRIÇÃO:
# Catálogo de livros que demonstra o uso de listas
# e dicionários para armazenar, consultar e filtrar
# dados estruturados.
# ==================================================      
# 

# --- LISTAS: CONCEITO BÁSICO ---

# Criando uma lista de títulos
titulos = [
    "O programador Pragmático",
    "Código limpo",
    "Entendendo Algoritmos",
]

# Acesso por indice (começa em C, não em 1!)
print("Primeiro livro:", titulos[0])
print("Último livro:", titulos[1])
print("Total de livros:",len (titulos))

# --- MÉTODO DE LISTA ---

print("\n---Operações na lista---")

# Adicionar um item ao final 
titulos.append("Python Fluente")
print("Após append:",titulos)

# Verificar se um item existe
busca = "Código Limpo"
if busca in titulos:
    print(f'"(busca)" está no catálogo.')
else:
    print(f'"(busca)" não encontrado.')

# Ordenar a lista
titulos.sort()
print("Lista ordenada:", titulos)

# remover u item
titulos.remve("Entendendo Algoritmos")
print("Após remove:", titulos)

# ---DICIONÁRIOS: CONCEITO BÁSICO ---

# Um dicionario representa um livro com seus atributos
livro = {
    "titulo":    "O Programador Pragmático",
    "autor":     "Andrew Hunt",
    "ano":       1999,  #int,não string
    "dispnível": True,  # bool
}

# Acessando valores pelas chaves
print("Titulo:", livro["titulo"])
print("Autor :", livro["autor"])
print("Ano   :", livro["ano"])
print("Status:", "Disponível" if livro ["disponivel"] else "Emprestdo")

# --- MODIFICANDO E CONSULTANDO ---

# Atualizando um valor existente
livro["disponivel"] = False  # livro emprestado
print("\n Após empréstimo:", livro["disponivel"])

# Adicionando uma nova chave
livro["paginas"] = 352
print("paginas:", livro["paginas"])

#.get() - acesso seguro: retorna None (ou padrão) se a chave não existir
editora = livro.get("editora", "Não informada")
print("Editora;", editora)  # não lança keyError, retorna o padrão

# ---- CATÁLOGO: LISTA DE DICIONÁRIOS ----

catalogo = [

    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "ano": 1999,
     "disponivel": True},

    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "ano": 2008,
     "disponivel": False},

    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "ano": 2016,
     "disponivel": True},

]

print("=== Catálogo da Biblioteca ===")

print()


# Percorrendo cada livro com for
for livro in catalogo:

    status = "✅ Disponível" if livro["disponivel"] else "📕 Emprestado"

    print(f' {livro["titulo"]} ({livro["ano"]})')

    print(f' Autor: {livro["autor"]} | {status}')

    print(" " + "-" * 40)

    # ---- CONSULTAS E FILTROS ----

print("\n=== Livros disponíveis ===")

for livro in catalogo:
    if livro["disponivel"]:                 # filtra apenas os disponíveis
        print(f'  ✅ {livro["titulo"]}')


print("\n=== Busca por título ===")

busca = input("Digite o título (ou parte): ").lower()

encontrado = False

for livro in catalogo:

    if busca in livro["titulo"].lower():   # .lower() ignora maiúsculas/minúsculas
        print(f'  Encontrado: {livro["titulo"]} — {livro["autor"]}')
        encontrado = True

if not encontrado:
    print("  Nenhum livro encontrado com esse termo.")


print("\n=== Atributos do primeiro livro ===")

for chave, valor in catalogo[0].items():   # .items() retorna pares (chave, valor)
    print(f"  {chave}: {valor}")

# --- FIM DO CÓDIGO ---
