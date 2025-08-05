class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def verInformacoes(self):
        print(f'''
Informações Pessoais:
Nome: {self.nome}
Idade: {self.idade} anos
Altura: {self.altura} metros
''')

#     def __str__(self):
#         return f'''
# Informações Pessoais:
# Nome: {self.nome}
# Idade: {self.idade} anos
# Altura: {self.altura} metros
# '''


if __name__ == "__main__":
    pessoa1 = Pessoa("João", 30, 1.75)
    print(pessoa1.nome)
