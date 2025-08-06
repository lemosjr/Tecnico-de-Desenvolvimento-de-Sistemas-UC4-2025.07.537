class Funcionario:
    def __init__(self, nome, cpf, cargo):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        
        if self.cargo == "Gerente":
            self.salario = 5000
        elif self.cargo == "Supervisor":
            self.salario = 3000
        else:
            self.salario = 2000

    def mostrarInformacoes(self):
        print(
            f"Nome: {self.nome}, CPF: {self.cpf}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}")

    def getCpf(self):
        return self.cpf

    def setCpf(self, novoCpf):
        if len(novoCpf) == 11 and novoCpf.isdigit():
            self.cpf = novoCpf
        else:
            print("CPF inválido. Deve conter 11 dígitos.")

    def getNome(self):
        return self.nome

    def setNome(self, novoNome):
        self.nome = novoNome
