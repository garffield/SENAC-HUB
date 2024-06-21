from programa import clientecadastro
x = 1

while x != 0:
    print ('-------------------------------')
    x = int(input("Selecione a opção desejada: "))
    print("0 - SAIR\n1 - CADASTRAR CLIENTE ")

    if x == 1:
        clientecadastro()