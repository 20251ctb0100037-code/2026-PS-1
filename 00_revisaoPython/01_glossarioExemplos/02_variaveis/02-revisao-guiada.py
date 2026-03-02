# ===================================================================
# SISTEMA DE BIBLIOTECA                                             
# ===================================================================
# DISCIPLINA : Programação de Sistemas (PS)                         
# AULA       : 04 - Revisão: Estrutura de dados                     
# NOME       : Maísa Gabriele Bom                                   
# DATA       : 26/02/2026                                           
# ===================================================================
# REPOSITÓRIO: https://github.com/20251ctb0100037-code/2026-PS      
# ===================================================================
# DESCRIÇÃO  :                                                      
# Catálogo de livors que demostra o uso de listas e dicionarios     
# para armazenar, consultar e filtrar dados estruturados            
# ===================================================================
# CONCEITOS  : variáveis, tipos de dados, operadores, estruturas de 
# seleção e de reétição                                             
# ===================================================================
#                                                                   
# ENTRADA DE DADOS ==================================================

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
    "titulo":    "O Programador Pragmático"
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

# --- CATÁLOGO: LISTA DE DICIONÁRIOS ---
