from Funcionario import Funcionario

funcionarios = []

print("Sistema de Gerenciamento de Funcionários")
print()

while True:

    print("Menu de Opções")
    print("1. Cadastrar Funcionário")
    print("2. Listar Funcionários")
    print("0. Sair")

    op = input("Escolha uma opção: ")

    if op == "1":
        print("Cadastrar Novo Funcionário")

        nome = input("Digite o nome: ")
        salario = float(input("Digite o salário: "))
        cargo = input("Digite o cargo: ")

        novo_funcionario = Funcionario(nome, salario, cargo)
        funcionarios.append(novo_funcionario)

    elif op == "2":
        print("Lista de Funcionários Cadastrados:")

        print(funcionarios)
        for i, f in enumerate(funcionarios):
            print(f"{i+1}. Nome: {f.nome} - R$ {f.salario:.2f}")

        escolha = int(
            input("Digite o número do funcionário que deseja visualizar os detalhes:")) - 1

        if escolha < 0 or escolha >= len(funcionarios):
            print("Funcionário Não Encontrado!")
        else:
            print(funcionarios[escolha].exibir_dados())

    elif op == "3":
        print("Aumentar Salário de Todos os Funcionários")
        aumento = float(input("Digite o percentual de aumento: "))

        for f in funcionarios:
            f.dar_aumento(aumento)

        print("Aumento aplicado a todos os funcionários.")

    elif op == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

    input("Pressione Enter para continuar...")
