while True:
    nome = input("Informe seu nome")
    if nome.isdigit() or len(nome) < 6:
        print("Nome inválido, informe seu nome.")
    else:
        print(nome)
        break