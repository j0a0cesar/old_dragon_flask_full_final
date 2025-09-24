from .dado import Dado

class Personagem:
    atributos_nomes = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]

    def __init__(self):
        self.forca = 0
        self.destreza = 0
        self.constituicao = 0
        self.inteligencia = 0
        self.sabedoria = 0
        self.carisma = 0
        self.raca = None
        self.classe = None
        self.dado = Dado(6)
        self.estilo = 'classico'

    def to_dict(self):
        return {nome: getattr(self, nome) for nome in self.atributos_nomes}

    def gerar_atributos(self):
        atributos = []
        for _ in range(6):
            soma = sum(self.dado.rolar() for _ in range(3))
            atributos.append(soma)
        return atributos
