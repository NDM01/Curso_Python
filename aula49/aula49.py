"""
Nesta aula o tema abordado é:
Filter
"""
from dados import produtos, pessoas, lista


def filtrar(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False


nova_lista = filter(filtrar, pessoas)

for produto in nova_lista:
    print(produto)
