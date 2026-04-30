#===================================================================
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
# Este sistema calcula a média e situação dos alunos
#===================================================================
# CONCEITOS  : funções, parâmetros, retorno e escopo
# ==========================================

# ------------------------------
# FUNÇÃO 1 - Cálculo da média
# ------------------------------
def calcular_media(nota1, nota2):
    """Recebe duas notas e retorna a média aritmética."""
    return (nota1 + nota2) / 2


# --------------------------------------
# FUNÇÃO 2 - Verificação da situação
# --------------------------------------
def verificar_situacao(media):
    """
    Recebe a média e retorna:
    - 'Aprovado' se média >= 6.0
    - 'Recuperação' se média entre 4.0 e 5.9
    - 'Reprovado' se média < 4.0
    """
    if media >= 6.0:
        return "Aprovado"
    elif media >= 4.0:
        return "Recuperação"
    else:
        return "Reprovado"

# --------------------------------------
# FUNÇÃO 3 - Solicitação e validação
# --------------------------------------
def solicitar_notas(nome_aluno):
    """
    Solicita duas notas entre 0 e 10.
    Não aceita valores inválidos.
    Retorna as duas notas validadas.
    """

    while True:
        try:
            nota1 = float(input(f"Digite a primeira nota de {nome_aluno}: "))
            if 0 <= nota1 <= 10:
                break
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

    while True:
        try:
            nota2 = float(input(f"Digite a segunda nota de {nome_aluno}: "))
            if 0 <= nota2 <= 10:
                break
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

    return nota1, nota2


# --------------------------------------
# FUNÇÃO 4 - Geração do relatório
# --------------------------------------
def gerar_relatorio(nome, media, situacao):
    """
    Exibe o resultado formatado.
    Não utiliza variáveis globais.
    """
    print("\n--- RELATÓRIO ---")
    print(f"Aluno     : {nome}")
    print(f"Média     : {media:.2f}")
    print(f"Situação  : {situacao}")
    print("------------------\n")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():
    print("=== SISTEMA DE AVALIAÇÃO IFPR ===\n")

    for i in range(1, 4):
        print(f"\nCadastro do {i}º aluno")
        nome = input("Nome do aluno: ")

        nota1, nota2 = solicitar_notas(nome)
        media = calcular_media(nota1, nota2)
        situacao = verificar_situacao(media)

        gerar_relatorio(nome, media, situacao)

    print("Processamento finalizado.")


# Executa apenas se for o arquivo principal
if __name__ == "__main__":
    main()
