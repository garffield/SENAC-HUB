while True:
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    if senha == nome:
        print("Acesso negado, coloque uma senha diferente do seu nome.")
        continue
    else:
        print("Acesso Permitido")
        break