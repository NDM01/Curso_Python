"""
Nesta aula o tema abordado é:
Módulos padrão do Python
Módulos são arquivos .py (que contém código python) e servem para expandir
as funcionalidades padrão da linguaguem.
Todos os módulos padrão:
https://docs.python.org/3/py-modindex.html
Não é recomendado utilizar o * ao importar módulos
Exemplo:
from random import *
"""

import random


def randint(*args):
    return 'hahaha'


for i in range(10):
    print(random.randint(0, 10))
