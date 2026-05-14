# ===================================================
# Disciplina : Programação de Sistemas
# Aula       : 23 — Menu interativo e persistência de objetos
# Tipo       : Gabarito (Mão na Massa)
# Autor      : Profe. Berssa
# Data       : 2026
# Descrição  : Agenda de Contatos com menu, CRUD em memória
#               e dois formatos de persistência (.txt e binário).
#               Serve de modelo para o Sistema de Hotel para Pets V2.0.
#
# ===================================================

# ===================================================
# Arquivo    : agenda.py
# Autor      : Maísa G. Bom
# Descrição  : Agenda de Contatos com menu interativo
# ===================================================

import pickle

# -------------------------------
# CLASSE PRINCIPAL
# -------------------------------
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir(self):
        print("   Nome:", self.nome)
        print("   Telefone:", self.telefone)
        print("   Email:", self.email)

    def para_linha_txt(self):
        return f"{self.nome};{self.telefone};{self.email}"


# -------------------------------
# PERSISTÊNCIA
# -------------------------------
def salvar_em_txt(contatos, caminho="agenda.txt"):
    arq = open(caminho, "w", encoding="utf-8")
    for c in contatos:
        arq.write(c.para_linha_txt()+"\n")
    arq.close()
    print("✓ Contatos salvos em TXT!")

def carregar_de_txt(caminho="agenda.txt"):
    contatos = []
    try:
        arq = open(caminho, "r", encoding="utf-8")
        for linha in arq:
            partes = linha.strip().split(";")
            if len(partes) == 3:
                nome, tel, mail = partes
                contatos.append(Contato(nome, tel, mail))
        arq.close()
    except:
        print("Arquivo TXT não encontrado, começando vazio...")
    return contatos

def salvar_em_binario(contatos, caminho="agenda.bin"):
    with open(caminho, "wb") as arq:
        pickle.dump(contatos, arq)
    print("✓ Contatos salvos em BINÁRIO!")

def carregar_de_binario(caminho="agenda.bin"):
    try:
        with open(caminho, "rb") as arq:
            return pickle.load(arq)
    except FileNotFoundError:
        print("Arquivo BIN não encontrado, agenda vazia.")
        return []


# -------------------------------
# CRUD
# -------------------------------
def cadastrar(contatos):
    print("\n--- Novo contato ---")
    nome = input("Nome: ")
    tel = input("Telefone: ")
    mail = input("Email: ")
    contatos.append(Contato(nome, tel, mail))
    print("✓ Contato cadastrado!")

def listar(contatos):
    if len(contatos) == 0:
        print("(agenda vazia)")
        return
    print(f"\n--- Agenda ({len(contatos)} contatos) ---")
    for i, c in enumerate(contatos, 1):
        print(f"[{i}]")
        c.exibir()

def remover(contatos):
    listar(contatos)
    if not contatos: return
    try:
        idx = int(input("Número do contato a remover: ")) - 1
        removido = contatos.pop(idx)
        print("✓ Removido:", removido.nome)
    except:
        print("Erro ao remover contato (entrada inválida).")


# -------------------------------
# MENU PRINCIPAL
# -------------------------------
def menu():
    contatos = carregar_de_binario()
    while True:
        print("\n========= MENU AGENDA =========")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Remover")
        print("4 - Salvar TXT")
        print("5 - Salvar BIN")
        print("0 - Sair")
        op = input("Opção: ")

        if op == "1":
            cadastrar(contatos)
        elif op == "2":
            listar(contatos)
        elif op == "3":
            remover(contatos)
        elif op == "4":
            salvar_em_txt(contatos)
        elif op == "5":
            salvar_em_binario(contatos)
        elif op == "0":
            salvar_em_binario(contatos)   # salva antes de sair
            print("Saindo... até logo!")
            break
        else:
            print("Opção inválida, tente de novo.")


# -------------------------------
# PONTO DE ENTRADA
# -------------------------------
if __name__ == "__main__":
    menu()
