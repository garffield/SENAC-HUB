class Aluno():
    def __init__(self, name, matricula):
        self.name = name
        self.matricula = matricula
        
    def notas(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.media = (n1 + n2) / 2
        self.verif_nota()

    def verif_nota(self):
        if self.media >= 7:
            self.situacao = "Aprovado"
        elif self.media < 7 and self.media >= 4:
            self.situacao = "Exame"
        else:
            self.situacao = "Reprovado"

    def main(self):
        print("-" * 20)
        print(f"Aluno: {self.name} \nMatricula: {self.matricula}")
        print("-" * 20)
        print(f"Notas\nP1: {self.n1}\nP2: {self.n2} \nMedia: {self.media}")
        print(f"Situacao: ** {self.situacao} **")
        print("-" * 20)

x = Aluno('Gabriel', '102006032')
x.notas(7, 7)

x.main()