from programa import clientecadastro

while True:
    print ('-------------------------------')
    print("0 - SAIR\n1 - CADASTRAR CLIENTE ")
    x = int(input("Selecione a opção desejada: "))

    if x == 1:
        clientecadastro()
    if x == 0:
        break