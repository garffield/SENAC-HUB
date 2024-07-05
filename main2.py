from programa import *

while True: 
    print('-'*10 ,"BEM VINDO A FABRICA ARMAS",'-'*10)
    print("1 - CADASTRO PESSOAL")
    print("2 - CADASTRAR ARMAS")
    print("3 - CADASTRAR CLIENTE")
    print('-'*10 ,"BEM VINDO A FABRICA ARMAS",'-'*10)
    op = input("Digite aqui: ")
    os.system("cls")

    if op == 1: 
        x = CadastroPessoal.cadastro_pessoal()