def par(x):
    if (x % 2) == 0:
        return True
    else:
        return False
while True:
    num = int(input("Digite um numero: "))
    if par(num):
        print("É par.")
    else:
        print("É impar.")
        