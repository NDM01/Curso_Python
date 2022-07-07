"""
Nesta aula o tema abordado é:
Criando, lendo, escrevendo e apagando arquivos
https://docs.python.org/3/library/functions.html#open
w+ - Apaga tudo que está no arquivo e escreve apenas os file.write
a+ - Adiciona texto sem apagar o que está no arquivo
r+ - Permite ler o que está escrito no arquivo
Para remover um ficheiro. Exemplo:
import os
os.remove('nome do ficheiro')
"""

import json

d1 = {
    'Pessoa 1': {
        'nome': 'Daniel',
        'idade': '18',
    },
    'Pessoa 2': {
        'nome': 'Maria',
        'idade': '19',
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)

print(d1_json)