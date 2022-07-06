"""
Nesta aula o tema abordado é:
For / Else me Python
"""
variavel = ['Daniel Franca', 'Maria', 'Afonso']

for valor in variavel:
    if valor.lower().startswith('d'):
        continue
    print(valor)