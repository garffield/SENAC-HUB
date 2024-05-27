while True:
    op = int(input(" 1 - Cliente \n 0 - Sair\n :"))
    if (op==0):
        print("Sair")
        break
    if (op == 1):
        prod = 1
        soma = 0
        while(prod != 0):
            prod = int(input("Digite o valor do produto: "))
            soma = soma + prod
        print("Total: ", soma)
        valor = int(input("DIgite o valor em dinheiro: "))
        troco = valor - soma 
        print("Troco: ", troco)