# frutas = ["Banana", "Maçã", "Laranja", "Uva", "Pera"]

# frutas2 = frutas

# frutas2 = ["Manga", "Abacaxi", "Melancia"]

# print(frutas)
# print(frutas2)

from Funcionario import Funcionario

func1 = Funcionario("João", 3000, "Desenvolvedor")
func1.nome = "Cleberson"

func2 = func1
func2.nome = "Maria"
func2.salario = 4000
func2.cargo = "Gerente"

print(func1.exibir_dados())
