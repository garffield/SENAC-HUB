import os
class Funcionario():
    def __init__(self):
        pass
    
    def salario_liq(self):
        inss = 0.12
        self.salario_liquido = self.salario - (self.salario * inss)

    def main(self):
        self.nome = input("Informe o nome do funcionario: ")
        funcionario.salario = float(input("Digite o salário do funcionário: "))
        self.salario_liq()
        self.cargo = input("Informe o cargo do funcionario: ")
        os.system('cls')
        print("-"*20)
        print(f"Nome do funcionario: {self.nome}")
        print("O salário líquido do funcionário é: ", self.salario_liquido)
        print("O cargo do funcionario é: ", self.cargo)
        print("-"*20)

funcionario = Funcionario()
funcionario.main()