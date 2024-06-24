from programa import clientecadastro
from programa import peçacadastro
from programa import servicocadastro
from programa import veiculocadastro
from programa import fornecedores
from programa import contaspendentes


x = 1

while x != 0:
    print ('-------------------------------')
    print("0 - SAIR\n1 - CLIENTE\n2 - PEÇAS\n3 - VEICULO\n4 - SERVIÇOS\n5 - FORNECEDORES (INCOMPLETO)\n6 - CONTAS A PAGAR ")
    print ('-------------------------------')
    x = (input("Selecione a opção desejada: "))

    if x == '1':
        clientecadastro()
    elif x == '2':
        peçacadastro()
    elif x == '3':
        veiculocadastro()
    elif x == '4':
        servicocadastro()
    elif x == '5':
        fornecedores()
    elif x == '6':
        contaspendentes()
    else:
        print("Informe um numero dentro dos parâmetros")