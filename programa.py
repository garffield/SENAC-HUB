import os
class CadastroPessoal():
    def __init__(self):
        pass

    def cadastro_pessoal(self):
    
        print("--> Bem vindo a area de cadastro <--")
        self.nome = input("Informe seu nome: ")
        self.__senha = input("Informe sua senha: ")
        self.matricula = input("Informe sua matricula: ")
        self.__fone = int("Informe seu telefone: ")
        self.__email = input("Informe seu email: ")
        self.__endereço = input("Informe seu endereço: ")
        print("Cadastro feito com sucesso")

        
    def cadastro_armas(self):
        print("--> Bem vindo ao cadastro de armas <--")
        self.tipo = input("Informe o tipo da arma: ")
        self.__num_serie = input("Informe o numero de série da arma: ")
        self.calibre = input("Informe o calibre da arma: ")
        self.valor = input("Informe o valor da arma: ")
        self.fabricação = input("Informe o ano de fabricação: ")
        self.marca = input("Informe a marca da arma: ")
        print("Cadastro feito com sucesso")
    
    def cadastro_cliente(self):
        print("--> Bem vindo a area de cadastro <--")
        self.__nome_cliente = input("Informe o nome do cliente: ")
        self.__cpf_cliente = input("Informe o CPF do cliente: ")
        self.__nascimento_cliente = input("Informe o ano de nascimento do cliente: ")
        self.__sexo_cliente = input("Informe o sexo do cliente: ")
        self.__endereço_cliente = input("Informe o endereço do cliente: ")
        self.__salario_cliente = input("Informe o salario do cliente: ")
        print("Cadastro feito com sucesso")

    def relatorio(self):
        print("---> RELATÓRIO <--")
        while True:
            op = input("Qual relatório deseja ver ?\n1 - Pessoal\n2 - Armas\n3 - Cliente \nDigite aqui: ")
            
            if op == 1:
                print("RELATÓRIO PESSOAL\n")
                print(f"Nome: {self.nome}")
                print(f"Senha: {self.__senha}")
                print(f"Matricula: {self.matricula}")
                print(f"Telefone {self.__fone }")
                print(f"Email: {self.__email}")
                print(f"Endereço: {self.__endereço}")

            elif op == 2:
                print("RELATÓRIO ARMA\n")
                print(f"Tipo: {self.tipo}")
                print(f"Num Série: {self.__num_serie}")
                print(f"Calibre: {self.calibre}")
                print(f"Valor: {self.valor}")
                print(f"Ano de fabricação: {self.fabricação}")
                print(f"Marca: {self.marca}")
            
            elif op == 3: 
                print("RELATÓRIO CLIENTE")
                print(f"Nome: {self.__nome_cliente}")
                print(f"CPF: {self.__cpf_cliente}")
                print(f"Ano de Nascimento: {self.__nascimento_cliente}")
                print(f"Sexo: {self.__sexo_cliente}")
                print(f"Endereço: {self.__endereço_cliente}")
                print(f"Salário: {self.__salario_cliente}")

            else:
                print("Informe uma opção válida")