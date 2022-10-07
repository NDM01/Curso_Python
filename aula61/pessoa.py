class Pessoa:
    def __init__(self, nome, idade, comer=False, falar=False):
        self.nome = nome
        self.idade = idade
        self.comer = comer
        self.falar = falar

    def comer(self, alimento):
        if self.comer:
            print(f'{self.nome} já está a comer')
            return

        print(f'{self.nome} está a comer {alimento}.')
        self.comer = True

    def parar_comer(self):
        if not self.comer:
            print(f'{self.nome} não está a comer')
            return

        print(f'{self.nome} parou de comer.')
        self.comer = False
