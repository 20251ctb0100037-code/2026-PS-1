"""
validador.py
Funções para validar entradas do usuário.
"""


def validar_numero(valor_str, minimo=None, maximo=None):
    """
    Valida se a string pode ser convertida para float
    e se está dentro dos limites.
    """

    try:
        valor = float(valor_str)
    except ValueError:
        return False, "Entrada inválida. Digite um número."

    if minimo is not None and valor < minimo:
        return False, f"O valor deve ser maior ou igual a {minimo}"

    if maximo is not None and valor > maximo:
        return False, f"O valor deve ser menor ou igual a {maximo}"

    return True, valor