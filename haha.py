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