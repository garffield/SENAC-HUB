class Retangulo():
    def __init__(self):
        pass

    def area(self):
        while True:
            try:
                self.altura = float(input("Digite a altura do Retangulo (AREA): "))
                self.largura = float(input("Digite a largura do Retangulo (AREA): "))
                print(self.altura * self.largura)
                break
            except ValueError:
                print("Valor invalido")

    def perimetro(self):
        while True:
            try:
                self.altura = float(input("Digite a altura do Retangulo (PERIMETRO): "))
                self.largura = float(input("Digite a largura do Retangulo (PERIMETRO): "))
                print(2 * (self.altura + self.largura))
                break
            except ValueError:
                print("Valor inválido")