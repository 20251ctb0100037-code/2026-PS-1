"""
formatador.py
Funções para formatar valores exibidos ao usuário.
"""

def formatar_numero(valor, casas=2):
    """
    Formata um número com um número definido de casas decimais.
    
    Args:
        valor (float): número a ser formatado
        casas (int): quantidade de casas decimais
        
    Returns:
        str: número formatado
    """
    return f"{valor:.{casas}f}"