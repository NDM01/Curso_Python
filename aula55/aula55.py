"""
Nesta aula o tema abordado é:
Como criar módulos em Python
"""
import math

PI = math.pi


def dobro_lista(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for i in lista:
        r *= 1
    return r


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobro_lista(lista))
    print(multiplica(lista))
    print(PI)
