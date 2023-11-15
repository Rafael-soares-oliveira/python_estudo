"""Exemplo de docstrings"""

"""Soma x e y

Este módulo contém funções e exemplos de documentação de funções.

:param x: Número 1
:type x: int or float
:param y: Número 2
:type y: int or float

:return: A soma entre x e y
:rtype: int or float
"""

def soma(x,y) -> float:
    """Função que irá somar dois valores
    
    :raises ValueError: Caso não seja inserido valor númerico inteiro ou float
    """
    return x + y