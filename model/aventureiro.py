from .personagem import Personagem
from .dado import Dado

class Aventureiro(Personagem):
    def __init__(self):
        super().__init__()
        self.estilo = 'aventureiro'
        self.dado = Dado(6)

    def gerar_atributos(self):
        atributos = []
        for _ in range(6):
            soma = sum(self.dado.rolar() for _ in range(3))
            atributos.append(soma)
        return atributos
