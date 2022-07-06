"""
Nesta aula o tema abordado são:
Expressões lambda (funções anônimas)
"""
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 8],
    ['P4', 50],
    ['P5', 3],

]
print(sorted(lista, key=lambda i: i[1], reverse=False))
print(lista)
