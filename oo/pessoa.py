class Pessoa:
    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p,7))
    print(id(p))
    print(p.cumprimentar(7))