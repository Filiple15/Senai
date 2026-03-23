class Cliente:
    def __init__(self, nome, email, idade, data_nasc, genero):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.data_nasc = data_nasc
        self.genero = genero

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Idade: {self.idade}")
        print(f"Data de nascimento: {self.data_nasc}")
        print(f"Gênero: {self.genero}")