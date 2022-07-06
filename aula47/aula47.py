"""
Nesta aula o tema abordado é:
Como agrupar de um dicionário
"""
from itertools import groupby, tee

alunos = [
    {'nome': 'Daniel', 'nota': 'A'},
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'Afonso', 'nota': 'A'},
    {'nome': 'Rui', 'nota': 'C'},
    {'nome': 'Cátia', 'nota': 'D'},
    {'nome': 'Pedro', 'nota': 'B'},
    {'nome': 'Sofia', 'nota': 'C'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupado, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'Categoria: {agrupado}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram nota {agrupado}')
    print()

