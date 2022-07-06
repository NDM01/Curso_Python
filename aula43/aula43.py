"""
Nesta aula o tema abordado é:
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import count

indice = count()
cidades = ['Porto', 'Lisboa', 'Coimbra', 'Faro', 'Alentejo']
estado = ['P', 'L', 'C', 'F', 'A']

cidades_estado = zip(
    indice,
    estado,
    cidades
)

for indice, estado, cidade in cidades_estado:
    print(indice, estado, cidade)

