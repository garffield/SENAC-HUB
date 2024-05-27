cont = 0

x = int(input("Digite um valor: "))
while x >= 0:
    x = x - 1
    print (x)
    cont = cont + 1
    if x == 0:
        break

print ("O numero foi reduzido", cont, " vezes.")