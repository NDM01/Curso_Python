"""
Nesta aula o tema abordado é:
Levantando exceções em Python
https://docs.python.org/3/library/exceptions.html
"""


def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0.')
    return n1 / n2


try:
    print(divide(n1=2, n2=0))
except ValueError as error:
    print(error)
