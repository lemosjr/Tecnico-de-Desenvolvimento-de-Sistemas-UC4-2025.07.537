from Pessoa import Pessoa

pessoa1 = Pessoa("Maria", 17, 1.65, 70, "Feminino")
pessoa2 = Pessoa("João", 30, 1.80, 80)

pessoa1.verInformacoes()
pessoa2.verInformacoes()


if (pessoa1.validarIdade()):
    print("Pessoa 1 é maior de idade")
else:
    print("Pessoa 1 é menor de idade")