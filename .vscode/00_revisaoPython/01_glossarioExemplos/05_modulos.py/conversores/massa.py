"""
massa.py
Funções de conversão de massa.
"""


def kg_para_libras(kg):
    """
    Converte quilogramas para libras.
    """
    return kg * 2.20462


def kg_para_gramas(kg):
    """
    Converte quilogramas para gramas.
    """
    return kg * 1000


# bloco de teste do módulo
if __name__ == "__main__":
    print("Testando módulo massa")
    print("1 kg em libras:", kg_para_libras(1))
    print("1 kg em gramas:", kg_para_gramas(1))