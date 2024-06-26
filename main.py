from programa import clientecadastro
from programa import peçacadastro
from programa import servicocadastro
from programa import veiculocadastro
from programa import fornecedores
from programa import contaspendentes
from programa import relatorio



while True:
    print ('-------------------------------')
    print("0 - SAIR\n1 - CADASTRAR CLIENTE\n2 - CADASTRAR PEÇAS\n3 - CADASTRAR VEICULO\n4 - SERVIÇOS DA OFICINA\n5 - CADASTRAR FORNECEDOR (INCOMPLETO)\n6 - CONTAS A PAGAR (INCOMPLETO)\n7 - RELATÓRIO ")
    print ('-------------------------------')
    try:
        x = int(input("Selecione a opção desejada: "))

        if x == 1:
            clientecadastro()
        elif x == 2:
            peçacadastro()
        elif x == 3:
            veiculocadastro()
        elif x == 4:
            servicocadastro()
        elif x == 5:
            fornecedores()
        elif x == 6:
            contaspendentes()
        elif x == 0:
            break
        elif x == 7:
            print("RELATÓRIO")
            relatorio()
        else:
            print("Informe um numero dentro dos parâmetros")
    except ValueError:
        print("Informe um numero dentro dos parâmetros")