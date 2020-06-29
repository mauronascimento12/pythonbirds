class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=13):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    silva = Pessoa(nome='Silva')
    mauro = Pessoa(silva, nome='Mauro')
    print(Pessoa.cumprimentar(mauro))
    print(id(mauro))
    print(mauro.cumprimentar())
    print(mauro.nome)
    print(mauro.idade)
    for filhos in mauro.filhos:
        print(filhos.nome)
    mauro.sobrenome = 'nascimento'
    del mauro.filhos
    mauro.olhos =  1
    print(mauro.__dict__)
    print(silva.__dict__)
    print(Pessoa.olhos)
    print(mauro.olhos)
    print(silva.olhos)
    print(id(Pessoa.olhos), id(mauro.olhos), id(silva.olhos))
