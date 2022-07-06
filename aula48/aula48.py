"""
Nesta aula o tema abordado é:
Map
Quando se usa o map e precisamos de o mostrar em um print é preciso usar o list para passar para lista. Exemplo:
print(list(nova_lista))
"""

from dados import produtos, pessoas, lista


# nova_lista = map(lambda x: x * 2, lista)
# ou
# nova_lista = [x * 2 for x in lista]

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p


nomes = map(aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)
