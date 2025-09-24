from .raca import Raca

class Elfo(Raca):
    def __init__(self):
        super().__init__()
        self.alinhamento = "Neutro"
        self.infravisao = "18 metros"
        self.movimento = 9
        self.habilidades_raca = [
            "Percepção Natural: Chance de detectar portas secretas.",
            "Graciosos: Bônus de +1 em testes de Destreza.",
            "Arma Racial: Bônus de +1 nos danos com arcos.",
            "Imunidades: Imune a sono e paralisia de Ghoul."
        ]
        self.peso_base = 60.0
