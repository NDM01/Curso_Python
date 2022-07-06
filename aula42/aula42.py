"""
Nesta aula o tema abordado é:
Comportamento de geradores e iteradores
lists, tuples, str -> Sequences -> Iterável
"""
nome = 'Daniel Franca'
iterador = iter(nome)
gerador = (letra for letra in nome)

for letra in gerador:
    print(letra)

# try:
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#
# except:
#     pass

# print('Sem valores')
# for valor in iterador:
#     print(valor)
