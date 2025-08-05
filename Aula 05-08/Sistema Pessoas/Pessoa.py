class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

if __name__ == "__main__":
    pessoa1 = Pessoa("João", 30, 1.75)
    print(pessoa1.nome)