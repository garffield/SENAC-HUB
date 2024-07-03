from conta import *

while True:
    print("Informe a operação:")
    var = int(input(("0 - SAIR\n1 - CADASTRO\n2 - EXTRATO\n3 - DEPOSITO\n4 - SAQUE\nDigite aqui: ")))

    if var == 0:
        break
    
    elif var == 1:
        x = Conta() # NOME, SALDO, CPF, SENHA
        x.cadastro()

    elif var == 2:
        x.verificar_senha()
        x.extrato()

    elif var == 3:
        x.depositar()

    elif var == 4:
        x.verificar_senha()
        x.sacar()

    else:
        print("Informe um valor válido")
        continue

    