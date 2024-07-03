class Conta():
    def __init__(self):
       pass

    def cadastro(self):
        print("Area de Cadastro")
        self.nome = input("Informe seu nome: ")
        self.__cpf = input("Informe seu CPF: ")
        self.__saldo = float(input("Informe seu saldo: "))
        self.__senha = input("Crie uma senha: ")
        print("Cadastro feito com sucesso")
    
    def extrato(self):
        senha_verif = input("Informe sua senha: ")
        if senha_verif == self.__senha:
            print(f"Olá {self.nome}, seu saldo é de R${self.__saldo}")
        else: 
            print("Senha incorreta")

    def depositar(self):
        deposito = float(input("Informe o valor a ser depositado: "))
        if deposito > 0:
            self.__saldo += deposito
        else:
            print("Valor inválido, tente novamente")

    def sacar(self):
        saque = float(input("Informe o valor do saque: "))
        if saque > 0 and saque <= self.__saldo:
            self.__saldo -= saque
        else:
            print("Valor inválido, tente novamente")
   
    def verificar_senha(self): 
        senha_verif = input("Informe sua senha: ")
        if senha_verif == self.__senha:
            print("Senha correta")
        else: 
            print("Senha incorreta")

            