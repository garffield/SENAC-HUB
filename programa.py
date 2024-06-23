Cliente_Cadastro = {}
PeçaCadastro = {}
VeiculoCadastro = {}
ServicoCadastro = {}
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

    '''
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
    '''

def peçacadastro():
    while True: #NOME
        nome = input("Informe o nome da peça: ")
        if nome.isdigit():
            print("Informe um nome válido: ")
        else:
            break
    while True: #NUMERO
        try:
            numero = int(input("Informe o numero da peça: "))
            break
        except ValueError:
            print("Informe apenas numeros")
    while True: #MODELO
        modelo = input("Informe o modelo da peça: ")
        break
    while True: #MARCA:
        marca = input("Informe a marca da peça: ")
        if len(marca) > 15: 
            print("Informe um valor válido")
        else:
            break
    while True: #TIPO DE PEÇA
        tipo = input("Informe o tipo de peça: ")
        break
    while True: #QTD STOCK
        
        try:
            qtd = int(input("Informe a quantidade em stock: "))
            if qtd < 0:
                break
            else:
                break
        except ValueError:
            print("Informe apenas numeros")
    while True: #PREÇO
        try:
            preco = float(input("Informe o preco da peça: R$"))
            if preco < 0:
                print("Valor inválido")
            else: 
                break
        except ValueError:
            print("Informe apenas numeros")
    while True: #DATA DE COMPRA
        data = input("Informe a data de compra (DD/MM/AAAA): ")
        if '/' in data:
            break
        else: 
            print("Informe uma data válida")
    while True: #LOCAÇÃO
        locacao_y_n = input("Deseja fazer a locação de alguma peça? (S/N): ")
        if locacao_y_n == 'S':
            locacao = input("Digite o nome da peça: ")
            break
        elif locacao_y_n == 'N':
            locacao = 'Nenhuma'
            break
        else: 
            print("Informe apenas S ou N")
    while True: #NOTAS
        notas = input("Informe alguma nota ou observação: ")
        break

    PeçaCadastro['Nome da peça'] = nome
    PeçaCadastro['Numero da peça'] = numero
    PeçaCadastro['Modelo da peça'] = modelo
    PeçaCadastro['Marca da peça'] = marca
    PeçaCadastro['Tipo da peça'] = tipo
    PeçaCadastro['Quantidade de peças'] = qtd
    PeçaCadastro['Preço da peça'] = preco
    PeçaCadastro['Data de compra'] = data
    PeçaCadastro['Locação? '] = locacao
    PeçaCadastro['Notas'] = notas

def veiculocadastro():
    while True: #MARCA
        marca = input("Informe a marca do veiculo: ")
        if marca == '':
            print("Informe uma marca válida")
        else: 
            break
    while True: #MODELO
        modelo = input("Informe o modelo do veiculo: ")
        if modelo == '':
            print("Informe um modelo válido: ")
        else: 
            break
    while True: #ANO
        ano = int(input("Informe o ano do veiculo: "))
        if ano > 2024 or ano < 1930:
            print("Informe um ano válido")
        else: 
            break
    while True:
        placa = input("Informe a placa do veiculo: ")
        if placa == '' or len(placa) > 7:
            print("Informe uma placa válida")
        else:
            break
    