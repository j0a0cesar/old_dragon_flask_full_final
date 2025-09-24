from .personagem import Personagem
from .dado import Dado

class Heroico(Personagem):
    def __init__(self):
        super().__init__()
        self.estilo = 'heroico'
        self.dado = Dado(6)

    def gerar_atributos(self):
        atributos = []
        for _ in range(6):
            rolagens = [self.dado.rolar() for _ in range(4)]
            rolagens.remove(min(rolagens))
            atributos.append(sum(rolagens))
        return atributos
