"""
O tema abordado nesta aula é:
Problemas dos parâmetros mutáveis em funções
Mutável: Listas, dicionários
Multilevel: Tuplas, strings, números, True, False, None
"""


def lista_clientes(clientes_i, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_i)
    return lista


lista_clientes1 = ['Fábio']
clientes1 = lista_clientes(['Daniel', 'Maria', 'Eduardo'])
clientes2 = lista_clientes(['Afonso', 'João', 'Pedro'])
clientes3 = lista_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)