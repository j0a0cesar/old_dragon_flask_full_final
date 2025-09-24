from .personagem import Personagem

class Classico(Personagem):
    def __init__(self):
        super().__init__()
        self.estilo = 'classico'
