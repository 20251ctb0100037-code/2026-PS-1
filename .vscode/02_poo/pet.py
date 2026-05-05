'''
-arquivo: pet.py
-disciplina: PS
-aula 20 - POO
-autor: Maísa G. Bom
-conceitos: classe, objeto, método, encapsulamento
-atividade: classe pet
-obs: pass serve para marcar um lugar de código e não executar o trecho ainda
'''
class Pet:
    '''
    classe que não guarda os dados do pet em um dicionário solto mas
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

    def exibir_dados(self):
        print("\n---Dados do Pet---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade}")
        print(f"Vacinado: {self.vacinado}")
        print(f"Dono: {self.dono}")
        print(f"Raça: {self.raca}")
        print(f"Peso: {self.peso} kg")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")

    def alterar_hospedagem(self, status):
        '''
        altera o estado de hospedagem do pet
        '''
        if self.hospedado == status:
            estado = "já está hospedado" if status else "não está hospedado"
            print(f"{self.nome} {estado}.")
        else:
            self.hospedado = status
            acao = "entrou no hotel" if status else "saiu do hotel"
            print(f"{self.nome} {acao}.")

    def registrar_entrada(self):
        self.alterar_hospedagem(True)

    def registrar_saida(self):
        self.alterar_hospedagem(False)

    def calcular_diaria(self):
        if self.idade > 20:
            print(f"{self.nome} não pode se hospedar no hotel por ter mais de 30 anos.")
            return None  # indica que não há diária calculada
        
        if self.idade <= 3:
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


# TESTES
'''
aqui chama o init (que é o construtor das classes) 
para mostrar os objetos pet1, pet2 e pet3 com os dados fornecidos 
'''
pet1 = Pet("Maia", "Cachorro", 1, True, "Angelo", "Pastor Alemão", 20)
pet2 = Pet("Mitz", "Gato", 11, True, "Maísa", "Angorá", 5)
pet3 = Pet("Feijão", "Cachorro", 21, False, "Pedro", "Vira-lata", 15)

pet1.exibir_dados()
pet1.registrar_entrada()
pet1.registrar_saida()
pet1.calcular_diaria()
pet1.verificar_vacinacao()
pet1.atualizar_peso(21)
pet1.emitir_resumo()

pet2.exibir_dados()
pet2.registrar_entrada()
pet2.registrar_saida
pet2.calcular_diaria()
pet2.verificar_vacinacao()
pet2.atualizar_peso(6)
pet2.emitir_resumo()

pet3.exibir_dados()
pet3.registrar_saida() 
pet3.registrar_entrada()
pet3.calcular_diaria()
pet3.verificar_vacinacao()
pet3.atualizar_peso(16)
pet3.emitir_resumo()
