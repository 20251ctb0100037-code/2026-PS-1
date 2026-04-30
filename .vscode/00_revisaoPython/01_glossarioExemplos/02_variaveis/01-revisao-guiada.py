# ===================================================================
# SISTEMA DE APROVAÇÃO DE ALUNOS                                    =
# ===================================================================
# DISCIPLINA : Programação de Sistemas (PS)                         =
# AULA       : 04 - Revisão: Variáveis, Tipos e Controle de Fluxo   =
# NOME       : Maísa Gabriele Bom                                   =
# DATA       : 24/02/2026                                           =
# ===================================================================
# REPOSITÓRIO: https://github.com/20251ctb0100037-code/2026-PS      =
# ===================================================================
# DESCRIÇÃO  :                                                      =
# Este programa determina a situação de cada aluno com base nas     =
# notas deles ( se o aluno será Aprovado, esta e recuperação ou foi =
# Reprovado).                                                       =
# ===================================================================
# CONCEITOS  : variáveis, tipos de dados, operadores, estruturas de =
# seleção e de reétição                                             =
# ===================================================================
#                                                                   =
# ENTRADA DE DADOS ==================================================
print("=============================================================")
print("=========== * SISTEMA DE APROVAÇÃO DE ALUNOS * ==============")
print("=============================================================")
print("=============== * DIGITE O NOME DO ALUNO * ==================")
nome = input(" ") #string para entrada de texto
print("=============================================================")
print("========== * DIGITE A NOTA 1 DO ALUNO (0 a 10) * ============")
nota1 = float(input("")) # str para a entrada de um número
print("=============================================================")
print("========== * DIGITE A NOTA 2 DO ALUNO (0 a 10) * ============")
nota2 = float(input(""))
print("=============================================================")
print("========== * DIGITE A NOTA 3 DO ALUNO (0 a 10) * ============")
nota3 = float(input(""))
#
media = (nota1 + nota2 + nota3) / 3 # calula a media do aluno 
if media >= 6.0: #compara o resultado com a situação
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperacao"
else: 
    situacao = "Reprovado"
#
print("=============================================================")
print(f"======== * O(A) ALUNO(A): {nome} TEM ESTA MÉDIA:{media:.2f} * ========")
print("=============================================================")
print("=============================================================")
print(f"============ * E ESTÁ NESTA SITUAÇÃO: {situacao} * ============")
print("=============-===============================================")