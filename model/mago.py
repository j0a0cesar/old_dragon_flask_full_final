from .classe import Classe

class Mago(Classe):
    def __init__(self):
        super().__init__(vida=4, ataque=0, protecao=5)
        self.armadura = "Nenhuma"
        self.armas = "Apenas armas pequenas"
        self.itens_magicos = "Pode usar todos os tipos de itens mágicos"
        self.habilidades_classe = {
            1: ["Magias Arcanas", "Ler Magias", "Detectar Magias"]
        }
