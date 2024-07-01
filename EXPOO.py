class LojaTenis():
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        
        try:
            self.nome == str(nome)
            self.idade == int(idade)
            self.telefone == int(telefone)
        except ValueError:
            print("Erro: dados inválidos")
    
    def alterar_cadastro(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

        try:
            self.nome == str(nome)
            self.idade == int(idade)
            self.telefone == int(telefone)
        except ValueError:
            print("Erro: dados inválidos")
    
    def relatorio(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nTelefone: {self.telefone} ")