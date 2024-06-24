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
        nome = input("Informe seu nome completo: ")
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
            if len(telefone) == 8 or telefone.isalpha():
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
        if data == '' or len(data) != 10 or data[2] != '/':
            print("Insira uma data válida")
        else: 
            break
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
    while True: #PLACA
        placa = input("Informe a placa do veiculo: ")
        if placa == '' or len(placa) > 7:
            print("Informe uma placa válida")
        else:
            break
    while True: #COR
        km = input("Informe a cor do veiculo: ")
        if km.isdigit():
            print("Informe uma cor, e não numeros")
        else:
            break
    while True: #CHASSI
        chassi = input("Informe o chassi do veiculo: ")
        if chassi == '' or len(chassi) > 17:
            print("Informe um chassi válido")
        else:
            break
    while True: #KM
        km = int(input("Informe o km do veiculo: "))
        if km < 0:
            print("Informe um km válido")
        else:
            break
    while True: #COMBUSTIVEL
        combustivel = input("Informe o combustivel do veiculo: ")
        if combustivel == '' or combustivel.isdigit():
            print("Informe um combustivel válido")
        else: 
            break
    while True: #TRANSMISSÃO
        transmissao = input("Informe a transmissão do veiculo: ")
        if transmissao == '' or transmissao.isdigit():
            print("Informe uma transmissão válida")
        else:
            break
    while True: #NOTAS
        notas = input("Observação a respeito do veiculo? (opcional) (ENTER CASO NÃO): ")
        if notas == '':
            notas = 'Nenhuma observação'
            break
        else:
            break

    VeiculoCadastro['Marca do veiculo'] = marca
    VeiculoCadastro['Modelo do veiculo'] = modelo
    VeiculoCadastro['Ano do veiculo'] = ano
    VeiculoCadastro['Placa do veiculo'] = placa
    VeiculoCadastro['Cor do veiculo'] = km
    VeiculoCadastro['Chassi do veiculo'] = chassi
    VeiculoCadastro['Km do veiculo'] = km
    VeiculoCadastro['Combustivel do veiculo'] = combustivel
    VeiculoCadastro['Transmissão do veiculo'] = transmissao
    VeiculoCadastro['Notas'] = notas

def servicocadastro():
    while True: #SERVIÇO
        servico = input("Informe o serviço realizado: ")
        if servico == '' or servico.isdigit():
            print("Informe um serviço válido")
        else:
            break
    while True: #VEICULO
        veiculo = input("Informe o veiculo que realizou o serviço: ")
        if veiculo == '' or veiculo.isdigit():
            print("Informe um veiculo válido")
        else:
            break
    while True: #DATA ENTRADA
        data_entrada = input("Informe a data de entrada do serviço (DD/MM/AAAA): ")
        if data_entrada == '' or len(data_entrada) != 10 or data_entrada[2] != '/':
            print("Informe uma data válida")
        else: 
            break
    while True: #DATA SAIDA
        data_saida = input("Informe a data de saida do serviço (DD/MM/AAAA): ")
        if data_saida == '' or len(data_saida) != 10 or data_saida[2]:
            print("Insira uma data válida")
        else:
            break
    while True: # MECANICO RESPONSAVEL
        mecanico = input("Informe o mecanico responsavel pelo serviço: ")
        if mecanico == '' or mecanico.isdigit():
            print("Informe um mecanico válido")
        else:
            break
    while True: #DESCRIÇÃO DO PROBLEMA
        descricao = input("Informe a descrição do problema: ")
        if descricao == '':
            descricao = 'Nenhuma descrição'
            break
        else:
            break
    while True: #PEÇAS UTILIZADAS
        pecas = input("Informe as peças utilizadas no serviço: ")
        if pecas == '':
            pecas = 'Nenhuma peça'
            break
        else:
            break
    while True: #FORMA DE PAGAMENTO
        forma_pagamento = input("Informe a forma de pagamento do serviço: ")
        if forma_pagamento == '' or forma_pagamento.isdigit():
            print("Informe uma forma de pagamento válida")
        else:
            break
    while True: # VALOR TOTAL
        valor_total = input("Informe o valor total do serviço: ")
        if valor_total == '' or valor_total.isalpha():
            print("Informe um valor total válido")
        else:
            break
    while True: #NOTAS
        notas = input("Informe as notas do serviço (ENTER PARA NADA): ")
        if notas == '':
            notas = 'Nenhuma nota'
        else:
            break
    
    ServicoCadastro['Serviço feito'] = servico
    ServicoCadastro['Veiculo'] = veiculo
    ServicoCadastro['Serviço feito'] = servico
    ServicoCadastro['Data de Entrada'] = data_entrada
    ServicoCadastro['Data de Saida'] = data_saida
    ServicoCadastro['Mecanico Responsavel'] = mecanico
    ServicoCadastro['Descricao do Problema'] = descricao
    ServicoCadastro['Pecas Utilizadas'] = pecas
    ServicoCadastro['Forma de Pagamento'] = forma_pagamento
    ServicoCadastro['Valor Total'] = valor_total
    ServicoCadastro['Notas'] = notas

def fornecedores():
    pass
def contaspendentes():
    pass
