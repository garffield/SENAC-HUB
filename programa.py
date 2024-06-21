Cliente_Cadastro = []
def clientecadastro():

    while True: #CPF
        try:
            cpf = input("Digite seu CPF (apenas números): ")
            if len(cpf) == 11:
                print("CPF válido.")
                break
            else:
                print("Por favor, digite um  CPF válido e com 11 dígitos.")
        except ValueError:
                print("Por favor, digite apenas números para o CPF.")    
    while True: #NOME
        nome_completo = nome("Digite seu nome completo: ")
        print("Nome válido, {0}. ".format(nome_completo))
        break    
    while True: #IDADE
        try:
            idade = int(input("Informe sua idade: "))
            if idade < 100:
                print("Idade válida. ")
                break
            else: 
                print("Digite uma idade válida!")
        except ValueError:
            print("Digite apenas numeros!")
    while True: #TELEFONE
        try:
            telefone = input("Informe seu telefone fixo: ")
            if len(telefone) == 8:
                print("Telefone válido !!")
                break
            else:
                print("Coloque um valor válido! (8 dígitos)")
        except ValueError:
            print("Digite um valor válido! (8 digitos)")
    while True: #PROFISSÃO
        prof = input("Informe sua profissão: ")
        if prof.isdigit():
            print("Profissão invalida.")
        else:
            break
    while True: #CELULAR
        try:
            celular = input("Informe seu Celular: ")
            if len(celular) == 11:
                print("Celular válido.")
                break
            else:
                print("Por favor, digite um  celular válido e com 11 dígitos.")
        except ValueError:
                print("Por favor, digite apenas números.") 
    while True: #EMAIL
        email = input("Informe seu email abaixo.")
        break
    while True: #SEXO
        sexo = input("Informe seu sexo: ")
        if sexo.isdigit():
            print("Sexo Inválido, Informe novamente.")
        else:
            break
    while True: #NOTAS
        notas = input("Alguma observação a ser feita?")
        if notas.isdigit():
            print("Apenas letras.")
        else:
            break
    while True: #DATA DO CADASTRO
        datacad = input("Informe a data de inclusão do cadastro. EX: '21 de Julho de 2024'")
        break                 

    Cliente_Cadastro.append(cpf)
    Cliente_Cadastro.append(nome_completo)
    Cliente_Cadastro.append(idade)
    Cliente_Cadastro.append(telefone)
    Cliente_Cadastro.append(prof)
    Cliente_Cadastro.append(celular)
    Cliente_Cadastro.append(email)
    Cliente_Cadastro.append(sexo)
    Cliente_Cadastro.append(notas)
    Cliente_Cadastro.append(datacad)
    
    while True:
        print("Deseja verificar alguma informação do seu cadastro? ")
        print("0 - CPF\n1 - NOME\n2 - IDADE\n 3 - TELEFONE\n4 - PROFISSÃO\n5 - CELULAR\n6 - EMAIL\n7 - SEXO\n8 - OBSERVAÇÕES\n9 - DATA DO CADASTRO\n10 - TODAS AS INFORMAÇÕES")
        verificarcad = int(input("Digite aqui: "))
        if verificarcad == 0:
            print(Cliente_Cadastro[0])
        elif verificarcad == 1:
            print(Cliente_Cadastro[1])
        elif verificarcad == 2:
            print(Cliente_Cadastro[2])
        elif verificarcad == 3:
            print(Cliente_Cadastro[3])
        elif verificarcad == 4:
            print(Cliente_Cadastro[4])
        elif verificarcad == 5:
            print(Cliente_Cadastro[5])
        elif verificarcad == 6:
            print(Cliente_Cadastro[6])
        elif verificarcad == 7:
            print(Cliente_Cadastro[7])
        elif verificarcad == 8:
            print(Cliente_Cadastro[8])
        elif verificarcad == 9:
            print(Cliente_Cadastro[9])
        elif verificarcad == 10:
            print(Cliente_Cadastro)
        
def is_alpha_space(str):
    return all(char.isalpha() or char.isspace() for char in str)
def nome(msg):
    while True:
        frase = input(msg)

        if not (is_alpha_space(frase) and len(frase) >= 12):
            # Se a frase não estiver válida, imprima a mensagem. Como não há
            # nada depois desse `print` a ser executado, o `while` continuará
            # a repetir este bloco até que o usuário digite um nome válido.
            print("Valores inválidos ou nome curto demais.")
        else:
            # Caso contrário (se o nome estiver válido), retorne-o. O `return`,
            # como encerra a função, também interromperá o `while`.
            return frase


clientecadastro()