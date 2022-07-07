"""
Nesta aula o tema abordado é:
Funções decoradoras e decoradores
"""

def master(funcao):
    def slave(*args, **kwargs):
        print('SIUUU')
        funcao(*args, **kwargs)

    return slave

@master
def oi():
    print('Hello World')

@master
def outra_func(msg):
    print(msg)

outra_func('Olá eu sou o Daniel')

