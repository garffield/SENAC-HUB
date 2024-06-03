
while True:
    print("Sistema de cadastro")
    try:
        x = int(input("1 - CADASTRO \n0 - ENCERRAR \n"))

    except ValueError:
        print("Tente apenas uma das duas opções.")



    else:
        if x == 1:
            nome = input("Digite seu nome: ")
            try:
                rg = int(input("Digite seu RG: "))
            except ValueError:
                print("Forneça apenas numeros para o RG")
            try:    
                idade = int(input("Digite sua idade: "))
            except ValueError:
                print("Digite apenas numeros para a idade")
                continue

        elif x == 0:
            print("Você escolheu sair.")
            break
        else: 
            print("Valor Invalido.")
