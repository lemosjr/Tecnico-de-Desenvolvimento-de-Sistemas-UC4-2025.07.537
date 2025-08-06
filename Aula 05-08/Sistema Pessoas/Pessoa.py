class Pessoa:

    def __init__(self, nome, idade, altura, peso, genero="Neutro"):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.genero = genero

    def verInformacoes(self):
        print(f'''
Informações Pessoais:
Nome: {self.nome}
Idade: {self.idade} anos
Altura: {self.altura} metros
Genero: {self.genero}
''')

    def validarIdade(self):
        if self.idade >= 18:
            return True
        else:
            return False

    def calcularIMC(self):
        imc = self.peso / (self.altura ** 2)
        return imc

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
