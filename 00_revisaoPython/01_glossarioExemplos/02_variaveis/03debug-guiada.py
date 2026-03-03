# Arquivo: 01b-debug.py

# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

def saudacao(nome, turno="manhã"):
    mensagem = f"Bom {turno}, {nome}!"
    return mensagem  # corrigido

saudacao("Ana")
print(saudacao("Bruno", "tarde"))

def dobrar(x):
    resultado = x * 2
    return resultado  # corrigido

print("Dobro de 5:", dobrar(5))

total = 0

def incrementar():
    global total      # corrigido
    total = total + 1

incrementar()
print("Total:", total)

def contagem(n):
    if n < 0:         # corrigido (caso base)
        return
    print(n)
    contagem(n - 1)

contagem(3)
