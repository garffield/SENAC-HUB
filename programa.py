Cliente_Cadastro = {}

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
        nome = input("Informe seu nome")
        if nome.isdigit() or len(nome) < 6:
            print("Nome inválido, informe seu nome novamente")
        else:
            print(nome)
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
        email = input("Informe seu email: ")
        if '@' in email:
            break
        else: 
            print("Email inválido")
            continue
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
   
    Cliente_Cadastro['Nome'] = nome
    Cliente_Cadastro['CPF'] = cpf
    Cliente_Cadastro['Idade'] = idade
    Cliente_Cadastro['Telefone'] = telefone
    Cliente_Cadastro['Profissão'] = prof
    Cliente_Cadastro['Celular'] = celular
    Cliente_Cadastro['Email'] = email
    Cliente_Cadastro['Sexo'] = sexo
    Cliente_Cadastro['Notas'] = notas
    Cliente_Cadastro['Data do cadastro'] = datacad

    while True:
        print("Deseja fazer alguma alteração? ")
        print("0 - NOME\n1 - CPF\n2 - IDADE\n3 - TELEFONE\n4 - PROFISSÃO\n5 - CELULAR\n6 - EMAIL\n7 - SEXO\n8 - OBSERVAÇÕES\n9 - DATA DO CADASTRO\n10 - NÃO ALTERAR NADA")
        alterarcad = int(input("Digite aqui: "))
        if alterarcad == 0:
            del Cliente_Cadastro[nome]
            nome = nome("Digite seu nome completo: ")
            Cliente_Cadastro['Nome'] = nome
            print(Cliente_Cadastro['Nome'])
        elif alterarcad == 1:
            print(Cliente_Cadastro['CPF'])
        elif alterarcad == 2:
            print(Cliente_Cadastro['Idade'])
        elif alterarcad == 3:
            print(Cliente_Cadastro['Telefone'])
        elif alterarcad == 4:
            print(Cliente_Cadastro['Profissão'])
        elif alterarcad == 5:
            print(Cliente_Cadastro['Celular'])
        elif alterarcad == 6:
            print(Cliente_Cadastro['Email'])
        elif alterarcad == 7:
            print(Cliente_Cadastro['Sexo'])
        elif alterarcad == 8:
            print(Cliente_Cadastro['Notas'])
        elif alterarcad == 9:
            print(Cliente_Cadastro['Data do cadastro'])
        elif alterarcad == 10:
            break   