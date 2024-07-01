class Conta():
    def __init__(self, numero, cpf, nome_titular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nome_titular = nome_titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
    def gerar_extrato(self):
        print(f'Numero: {self.numero}\nNome: {self.nome_titular}\nCPF: {self.cpf}\nSaldo: {self.saldo}')

