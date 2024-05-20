n1 = int(input("Digite o preço de um produto: "))
n2 = int(input("Digite o preço de um produto: "))
n3 = int(input("Digite o preço de um produto: "))

if n1 < n2 and n1 < n3:
    print (f'o produto 1 é mais barato')
elif n2 < n1 and n2 < n3:
    print (f'o produto 2 é mais barato')
elif n3 < n2 and n3 < n1:
    print (f'o produto 3 é mais barato')