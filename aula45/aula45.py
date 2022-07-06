"""
Nesta aula o tema abordado é:

count - Itertools
"""

from itertools import count

contador = count(start=5, step=0.1)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10:
        break

cont = count()
lista = ['Daniel', 'João', 'Maria']
lista = zip(cont, lista)
print(list(lista))