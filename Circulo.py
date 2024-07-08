class Circulo():
    def __init__(self):
        pass
    
    def area(self):
        while True:
            try:
                self.raio = float(input("Digite o raio do circulo (AREA): "))
                print(3.14 * self.raio ** 2)
                break
            except ValueError:
                print("Valor invalido")

    def perimetro(self):
        while True:
            try:
                self.raio = float(input("Digite o raio do circulo (PERIMETRO): "))
                print(2 * 3.14 * self.raio)
                break
            except ValueError:
                print("Valor inválido")
    