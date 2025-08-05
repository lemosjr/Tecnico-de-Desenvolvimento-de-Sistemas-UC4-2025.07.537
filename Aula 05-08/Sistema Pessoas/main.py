from Pessoa import Pessoa

listaFuncionarios = {
    "02": {"nome": "João", "idade": 30, "altura": 1.75},
    "01": {"nome": "Maria", "idade": 25, "altura": 1.80}
}


pessoa1 = Pessoa("Maria", 25, 1.65)
pessoa2 = Pessoa("João", 30, 1.80)
print(pessoa1.nome)
print(pessoa2.nome)
