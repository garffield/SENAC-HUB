class Pessoa():
    def __init__(self, nome, idade, endereco, cidade, estado):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
    def relatorio(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereco}")
        print(f"Cidade: {self.cidade}")
        print(f"Estado: {self.estado}\n")

class Aluno(Pessoa):
    def __init__(self, mensalidade, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.mensalidade = mensalidade 
        print("-" * 25)
        print("Seja bem vindo Aluno")
        super().relatorio()
        print ("Mensalidade: ", self.mensalidade)
        print("-" * 25)

class Professor(Pessoa):
    def __init__(self, salario, nome, idade, endereco, cidade, estado):
        super().__init__(nome, idade, endereco, cidade, estado)
        self.salario = salario
        print("-" * 25)
        print("Seja bem vindo Professor")
        super().relatorio()
        print ("Salário: ", self.salario)
        print("-" * 25)

x = Professor('1200.00', 'Ederson', '22', 'Aracaju', 'Campo Grande', 'MS')
y = Aluno('200.00', 'José', '17', 'Afonso Pena', 'Dourados', 'MS')
        