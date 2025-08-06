class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def exibir_dados(self):
        return f'''
Informações do Funcionário:

Nome: {self.nome}

Salário: R$ {self.salario:.2f}

Cargo: {self.cargo}

-----------//----------
'''
    def dar_aumento(self, percentual):
        self.salario = self.salario * (1 + percentual/100)
