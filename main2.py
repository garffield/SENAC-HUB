from programa import *

x = FABRICAARMA()

while True: 
    print('-'*10 ,"BEM VINDO A FABRICA ARMAS",'-'*10)
    print("1 - CADASTRO PESSOAL")
    print("2 - CADASTRAR ARMAS")
    print("3 - CADASTRAR CLIENTE")
    print("4 - RELATÓRIO")
    print("0 - SAIR")
    print('-'*10 ,"BEM VINDO A FABRICA ARMAS",'-'*10)
    op = input("Digite aqui: ")
    os.system("cls")

    if op == '1': 
        x.cadastro_pessoal()
    elif op == '2':
        x.cadastro_armas()
    elif op == '3':
        x.cadastro_cliente()
    elif op == '4':
        x.relatorio()
    elif op == '0':
        break
    else:
        print("Digite um valor válido")