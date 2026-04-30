"""
================================================
Sistema de Biblioteca 📚
Data: 18/03/2026
Autor: Maísa Gabriele
Descrição:
Sistema para gerenciamento de livros com:
- Cadastro
- Listagem
- Busca
- Empréstimo
- Devolução
- Persistência em arquivo (biblioteca.txt)
- Histórico de operações (historico.txt)
================================================
"""

import json
from datetime import datetime

# ------------------ DADOS -----------------------------------------------------------------------
catalogo = [] # lista de livros, cada livro é um dicionário com título, autor e disponibilidade

# ------------------ ARQUIVOS -----------------------------------------------------------------

def salvar_dados(): # salva os dados da variável catalogo no arquivo biblioteca.txt
    with open("biblioteca.txt", "w", encoding="utf-8") as f:
        json.dump(catalogo, f, ensure_ascii=False, indent=4)

def carregar_dados(): # carrega os dados do arquivo para a variável catalogo
    global catalogo
    try:
        with open("biblioteca.txt", "r", encoding="utf-8") as f:
            catalogo = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        catalogo = []

def registrar_historico(acao): # registra uma ação no histórico como empréstimo ou devolução
    with open("historico.txt", "a", encoding="utf-8") as f:
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        f.write(f"[{data}] {acao}\n")

# ------------------ FUNÇÕES ---------------------------------------------------------------------------------

def listar_livros(): # mostra a lista de livros cadastrados, indicando se estão disponíveis ou indisponíveis
    print("\n" + "=" * 50)
    print(" 📚 CATÁLOGO DA BIBLIOTECA 📚")
    print("=" * 50)

    if not catalogo:
        print("  Nenhum livro cadastrado.")
        return

    for i, livro in enumerate(catalogo, 1):
        status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"
        print(f"  {i}. {livro['titulo']} — {livro['autor']}   [{status}]")

    print("=" * 50)


def adicionar_livro(): # adiciona um livro novo 
    print("\n--- Adicionar Novo Livro ➕ ---")

    titulo = input("Título: ").strip()
    autor  = input("Autor : ").strip()

    if not titulo or not autor:
        print("⚠️ Título e autor são obrigatórios.")
        return

    # evitar duplicados
    for livro in catalogo:
        if livro["titulo"].lower() == titulo.lower():
            print("⚠️ Livro já cadastrado.")
            return

    catalogo.append({
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    })

    salvar_dados()
    print(f"✅ '{titulo}' adicionado com sucesso!")


def buscar_livro(): # busca por título ou autor e mostra os resultados encontrados
    print("\n--- Buscar Livro 🔎 ---")
    termo = input("Digite título ou autor: ").strip().lower()

    try:
        resultados = [
            l for l in catalogo
            if termo in l["titulo"].lower() or termo in l["autor"].lower()
        ]

        if not resultados:
            print("  Nenhum livro encontrado.")
            return

        print(f"\n  {len(resultados)} resultado(s):")
        for livro in resultados:
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f"  • {livro['titulo']} — {livro['autor']} [{status}]")

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


def registrar_emprestimo(): # registra o empréstimo de um livro e deixa ele indisponível
    listar_livros() # mostra a lista para o usuário escolher o livro

    if not catalogo:
        return

    print("\n--- Registrar Empréstimo 📝 ---")

    try:
        numero = int(input("Número do livro: "))

        if numero < 1 or numero > len(catalogo):
            print("⚠️ Número fora do intervalo.")
            return

        livro = catalogo[numero - 1]

        if not livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está emprestado.")
        else:
            livro["disponivel"] = False
            salvar_dados()
            registrar_historico(f"Empréstimo: {livro['titulo']}")
            print(f"✅ Empréstimo de '{livro['titulo']}' registrado.")

    except ValueError:
        print("❌ Entrada inválida. Digite apenas o número.")


def devolver_livro(): # registra a devolução de um livro e deixa ele disponível
    listar_livros() # mostra a lista para o usuário escolher o livro

    if not catalogo:
        return

    print("\n--- Registrar Devolução ↩️ ---")

    try:
        numero = int(input("Número do livro: "))

        if numero < 1 or numero > len(catalogo):
            print("❌ Número fora da lista.")
            return

        livro = catalogo[numero - 1]

        if livro["disponivel"]:
            print(f"⚠️ '{livro['titulo']}' já está disponível.")
        else:
            livro["disponivel"] = True
            salvar_dados()
            registrar_historico(f"Devolução: {livro['titulo']}")
            print(f"✅ Devolução de '{livro['titulo']}' registrada.")

    except ValueError:
        print("❌ Digite apenas o número.")
    except IndexError:
        print("❌ Número fora da lista.")


def ver_historico(): # mostra o histórico de operações feitas
    print("\n--- 📜 HISTÓRICO ---")

    try:
        with open("historico.txt", "r", encoding="utf-8") as f:
            conteudo = f.read()

            if not conteudo:
                print("Nenhuma operação registrada.")
            else:
                print(conteudo)

    except FileNotFoundError:
        print("Nenhum histórico encontrado.")


# ------------------ MENU ----------------------------------------

def menu(): # mostra o cabeçalho do programa
    print("=========================================")
    print("\n 📚 SISTEMA DE BIBLIOTECA 📚 v2")
    print("=========================================")

    opcoes = { #Mostra as opções que o usuário pode escolher
        "1": ("Listar livros 📑", listar_livros),
        "2": ("Adicionar livro ➕", adicionar_livro),
        "3": ("Buscar livro 🔎", buscar_livro),
        "4": ("Registrar empréstimo 📝", registrar_emprestimo),
        "5": ("Devolver livro ↩️", devolver_livro),
        "6": ("Ver histórico 📜", ver_historico),
        "0": ("Sair 🔙", None),
    }

    while True:  # mostra o menu até o usuário escolher sair
        print("\n Opções:")
        for chave, (descricao, _) in opcoes.items():
            print(f"  {chave}. {descricao}")

        try:
            escolha = input("Escolha uma opção: ").strip()

            if escolha not in opcoes:
                raise ValueError(f"Opção '{escolha}' inválida.")

        except ValueError as e:
            print(f"⚠️ {e}")
            continue

        if escolha == "0":
            print("\n Até logo! 👋")
            break

        _, funcao = opcoes[escolha]
        funcao()

# ------------------ EXECUÇÃO ------------------------------------------

if __name__ == "__main__": # verifica se o arquivo está funcionando
    carregar_dados()
    menu()

# --------------- FIM -----------------------------------