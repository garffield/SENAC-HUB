print('DIGITE 1 PARA SIM E 0 PARA NÃO\n')

x1 = int(input("Telefonou para a vítima? "))
x2 = int(input("Esteve no local do crime? "))
x3 = int(input("Mora perto da vítima? "))
x4 = int(input("Devia para a vítima? "))
x5 = int(input("Já trabalhou com a vítima? "))

y = x1 + x2 + x3 + x4 + x5
if y > 5:
    print("Digite um numero válido.")
if (y == 2):
    print("VOCÊ É UM POSSIVEL SUSPEITO.")
elif (y == 3 or y == 4):
    print("VOCÊ É CÚMPLICE!!")
elif (y == 0):
    print("INOCENTE")
else:
    print("ASSASSINO!!!!")