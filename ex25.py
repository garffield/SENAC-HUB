n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
n3 = int(input("Digite um numero: "))

if n1 > n2 and n1 > n3:
    print (f'{n1} é maior')
elif n2 > n1 and n2 > n3:
    print (f'{n2} é maior')
elif n3 > n2 and n3 > n1:
    print (f'{n3} é maior')

if n1 < n2 and n1 < n3:
    print (f'{n1} é menor')
elif n2 < n1 and n2 < n3:
    print (f'{n2} é menor')
elif n3 < n2 and n3 < n1:
    print (f'{n3} é menor')