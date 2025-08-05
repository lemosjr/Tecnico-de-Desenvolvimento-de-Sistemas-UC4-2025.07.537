# nome = "Pessoa"
# idade = 30
# altura = 1.75
# pessoa = ["Pessoa", 30, 1.75]
# pessoa = [nome, idade, altura]

pessoa = {
    "nome": "Pessoa",
    "idade": 30,
    "altura": 1.75
}

print(__name__)

if __name__ == "__main__":

    pessoa["nome"] = "Maicou"
    pessoa["cpf"] = "12345678901"
    pessoa["cpf"] = "abacate"
    print(pessoa)
