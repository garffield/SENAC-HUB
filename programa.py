import os
class FABRICAARMA():
    def __init__(self):
        pass

    def cadastro_pessoal(self):
        print("--> Bem vindo a area de cadastro <--")

        while True: # NOME
            self.nome = input("Informe seu nome: ")
            if self.nome.isdigit():
                print("Nome inválido")
                continue
            else:
                break

        os.system("cls")
        self.__senha = input("Informe sua senha: ")
        os.system("cls")
        self.matricula = input("Informe sua matricula: ")
        os.system("cls")

        while True: # TELEFONE
            self.__fone = input("Informe seu telefone: ")
            if self.__fone.isdigit():
                break
            else:
                print("Telefone inválido")
                continue
        
        os.system("cls")
        
        while True: #EMAIL
            self.__email = input("Informe seu email: ")
            if '@' and ".com" in self.__email:
                break
            else:
                print("Email inválido")
                continue
        
        os.system("cls")
        self.__endereço = input("Informe seu endereço: ")
        os.system('cls')
        
    def cadastro_armas(self):
        print("--> Bem vindo ao cadastro de armas <--")
        self.tipo = input("Informe o tipo da arma: ")
        
        os.system("cls")

        while True: #NUM SERIE    
            self.__num_serie = input("Informe o numero de série da arma: ")
            if self.__num_serie.isdigit():
                break
            else:
                print("Valor inválido")
                continue
        
        os.system("cls")
        self.calibre = input("Informe o calibre da arma: ")
        os.system("cls")
        
        while True: #VALOR
            self.valor = input("Informe o valor da arma: ")
            if self.valor.isdigit():
                break
            else:
                print("Valor inválido")
                continue
        
        os.system("cls")

        while True: #ANO FABRICAÇÂO
            self.fabricação = input("Informe o ano de fabricação: ")
            if (len(self.fabricação)) == 4:
                break
            else:
                print("Ano inválido")
                continue
        
        os.system("cls")
        self.marca = input("Informe a marca da arma: ")
        os.system('cls')     
    
    def cadastro_cliente(self):
        print("--> Bem vindo a area de cadastro <--")
        
        while True: #NOME
            self.__nome_cliente = input("Informe o nome do cliente: ")
            if self.__nome_cliente.isdigit():
                print("Nome inválido")
                continue
            else:
                break
        
        os.system("cls")

        while True: #CPF
            self.__cpf_cliente = input("Informe o CPF do cliente: ")
            if (len(self.__cpf_cliente)) == 11:
                break
            else:
                print("Valor inválido")
                continue
        
        os.system("cls")

        while True: #ANO NASCIMENTO
            self.__nascimento_cliente = input("Informe o ano de nascimento do cliente: ")
            if (len(self.__nascimento_cliente)) == 4:
                break
            else:
                print("Ano inválido")
                continue
        
        os.system("cls")
        self.__sexo_cliente = input("Informe o sexo do cliente: ")
        os.system("cls")
        self.__endereço_cliente = input("Informe o endereço do cliente: ")
        os.system("cls")

        while True: #SALARIO CLIENTE
            self.__salario_cliente = int(input("Informe o salario do cliente: "))
            if self.__salario_cliente < 0:
                print("Valor invalido")
                continue
            else:
                break

        os.system('cls')

    def relatorio(self):
        while True:
            op = input("---> RELATÓRIO <--\n1 - Pessoal\n2 - Armas\n3 - Cliente \n0 - SAIR\nDigite aqui: ")
            
            if op == '1':
                os.system('cls')
                print("RELATÓRIO PESSOAL")
                print(f"Nome: {self.nome}")
                print(f"Senha: {self.__senha}")
                print(f"Matricula: {self.matricula}")
                print(f"Telefone {self.__fone }")
                print(f"Email: {self.__email}")
                print(f"Endereço: {self.__endereço}")
                
            elif op == '2':
                os.system('cls')
                print("RELATÓRIO ARMA")
                print(f"Tipo: {self.tipo}")
                print(f"Num Série: {self.__num_serie}")
                print(f"Calibre: {self.calibre}")
                print(f"Valor: {self.valor}")
                print(f"Ano de fabricação: {self.fabricação}")
                print(f"Marca: {self.marca}")

            elif op == '3': 
                os.system('cls')
                print("RELATÓRIO CLIENTE")
                print(f"Nome: {self.__nome_cliente}")
                print(f"CPF: {self.__cpf_cliente}")
                print(f"Ano de Nascimento: {self.__nascimento_cliente}")
                print(f"Sexo: {self.__sexo_cliente}")
                print(f"Endereço: {self.__endereço_cliente}")
                print(f"Salário: {self.__salario_cliente}")
            
            elif op == '0':
                os.system('os')
                break
            
            else:
                print("Informe uma opção válida")

