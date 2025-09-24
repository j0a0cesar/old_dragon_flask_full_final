from .classe import Classe

class Guerreiro(Classe):
    def __init__(self):
        super().__init__(vida=10, ataque=1, protecao=5)
        self.armadura = "Pode usar todas as armaduras"
        self.armas = "Pode usar todas as armas"
        self.itens_magicos = "Limitado"
        self.habilidades_classe = {
            1: ["Aparar", "Maestria em Arma"],
            6: ["Ataque Extra"]
        }
