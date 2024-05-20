p1 = float(input("Informe o preço do produto: "))
p2 = float(input("Informe o preço do produto: "))
p3 = float(input("Informe o preço do produto: "))

if (p1 < p2 and p1 < p3):
    print("Você deve comprar o primeiro produto.")

elif (p2 < p1 and p2 < p3):
    print("Você deve comprar o segundo produto.")

else:
    print("Você deve comprar o terceiro produto.")