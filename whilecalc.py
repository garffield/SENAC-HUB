x = 1
while (x != 0):
    x = float(input(" 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 0 - Para Retornar interromper\n"))

    if (x > 4 or x < 0):
        print("Opção invalida.")
        continue

    if x == 1:
        n1 = int(input("Digite um numero para a operação de Adição: "))
        n2 = int(input("Digite um numero para a operação de Adição: "))
        resultado = n1 + n2
        print(resultado)
        
    if x == 2:
        n1 = int(input("Digite um numero para a operação de Subtração:"))
        n2 = int(input("Digite um numero para a operação de Subtração:"))
        resultado = n1 - n2
        print(resultado)
        
    if x == 3:
        n1 = int(input("Digite um numero para a operação de Multiplicação:"))
        n2 = int(input("Digite um numero para a operação de Multiplicação:"))
        resultado = n1 * n2
        print (resultado)
        
    if x == 4:
        n1 = float(input("Digite um numero para a operação de Divisão:"))
        n2 = float(input("Digite um numero para a operação de Divisão:"))
        resultado = n1 / n2
        print(resultado)
    if x == 0:
        break