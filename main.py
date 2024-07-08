from Circulo import *
from Retangulo import *
import os

x = Circulo()
y = Retangulo()

while True:
    op = input("1 - Circulo\n2 - Retangulo\n Digite aqui: ")
    if op == '1':
        while True:
            os.system('cls')
            print("CIRCULO")
            op = input("1 - Area\n2 - Perimetro\n Digite aqui: ") # CIRCULO
            if op == '1': 
                x.area()
                break
            elif op == '2':
                x.perimetro()
                break
            else:
                print("Opcao invalida")
    elif op == '2': # RETANGULO
        while True:
            os.system('cls')
            print("RETANGULO")
            op = input("1 - Area\n2 - Perimetro\n Digite aqui: ")
            if op == '1':
                y.area()
                break
            elif op == '2':
                y.perimetro()
                break
            else:
                print("Opcao invalida")
    else:
        os.system('cls')
        print("Opcao invalida")