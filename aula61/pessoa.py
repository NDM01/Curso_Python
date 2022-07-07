class Pessoa:
    def __int__(self, nome, idade, comer=False, falar=False):
        self.nome = nome
        self.idade = idade
        self.comer = comer
        self.falar = falar

    def comer(self, alimentos):
        print(f'{self.nome} está a comer {alimentos}')
        self.comer = True
