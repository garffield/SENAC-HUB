class Conta():
    def __init__(self, nome, saldo, cpf, senha):
        self.nome = nome
        self.__saldo = saldo
        self.__cpf = cpf
        self.__senha = senha

    def extrato(self):
        while True:
            conferir_senha = int(input("Informe sua senha: "))
            if conferir_senha == self.__senha:
                print(f"Olá {self.nome}, seu saldo é de R${self.__saldo}")
                break
            else:
                print("Senha incorreta, tente novamente")
                continue

    def depositar(self):
        while True:
            deposito = float(input("Informe o valor a ser depositado: "))
            if deposito > 0:
                self.__saldo += deposito
                break
            else:
                print("Valor inválido, tente novamente")
                continue
    
    def sacar(self):
        while True:
            saque = float(input("Informe o valor a ser sacado: "))
            if saque > 0 and saque <= self.__saldo:
                self.__saldo -= saque
                break
            else:
                print("Valor inválido, tente novamente")