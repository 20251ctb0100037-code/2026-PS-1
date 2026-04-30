'''
-arquivo: pet.py
-disciplina: PS
-aula 20 - POO
-autor: Maísa G. Bom
-conceitos: classe, objeto, método, encapsulamento
-atividade: classe pet
-obs: pass serve para marcar um luigar de código e 
não executar o trecho ainda
'''

class Pet:
    '''
    classe que não quarda os dados do pet em um dicionário solto mas
    agrupa os dados dentro de uma classe.
    '''

    def __init__(self, nome, especie, idade, vacinado, dono, raca, peso):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.vacinado = vacinado
        self.dono = dono
        self.peso = peso
        self.raca = raca
        self.hospedado = False

        '''
        metodo conscrutor:
        executado quando um novo objeto pet é criado
        ex: Parâmetro: self
        '''

    def exibir_dados(self):
        '''
        exibe os dados principais do pet como nome, idade e hospedagem
        '''

        print("\n---Dados do Pet---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Vacinado: {self.vacinado}")
        print(f"Dono: {self.dono}")
        print(f"Raça: {self.raca}")
        print(f"Peso: {self.peso} kg")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")

    def registrar_entrada(self):
        '''
        registra a entrada do pet no hotel e se o pet ainda não
        estiver hsopedado, muda o atributo hospedado para True
        '''
        if not self.hospedado:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel.")
        else:
            print(f"{self.nome} já está hospedado.")

    def registrar_saida(self):
        '''
        Registra a saída do pet do hotel e muda o atributo
        true para false
        '''
        self.hospedado = False
        print(f"{self.nome} saiu do hotel.")

    def calcular_diaria(self):
        if self.idade <= 3:#analiza a idade do pet e calcula a diaria
            valor = 50
        elif self.idade <= 10:
            valor = 60
        else:
            valor = 75

        print(f"A diária do pet {self.nome} é R$ {valor}")
        
        return valor
    
    def verificar_vacinacao(self):
        if self.vacinado:
            print(f"{self.nome} está vacinado.")
        else:
            print(f"{self.nome} NÃO está vacinado.")

    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso
        print(f"O peso de {self.nome} foi atualizado para {self.peso} kg.")

    def emitir_resumo(self):
        print(f"Nome: {self.nome} - Espécie: {self.especie} - Idade: {self.idade} - Peso: {self.peso} kg")



pet1 = Pet("Maia", "Cachorro", 1, True, "Angelo", "Pastor Alemão", 20)
pet2 = Pet("Mitz", "Gato", 6, True, "Maísa", "Angorá", 5)
pet3 = Pet("Feijão", "Cachorro", 5, False, "Pedro", "Vira-lata", 15)

pet1.exibir_dados()
pet1.registrar_entrada()
pet1.calcular_diaria()
pet1.verificar_vacinacao()
pet1.atualizar_peso(22)
pet1.emitir_resumo()
