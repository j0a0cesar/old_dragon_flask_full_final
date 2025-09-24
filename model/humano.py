from .raca import Raca

class Humano(Raca):
    def __init__(self):
        super().__init__()
        self.alinhamento = "Qualquer"
        self.infravisao = "Não possui"
        self.movimento = 9
        self.habilidades_raca = [
            "Aprendizado: +10% XP.",
            "Adaptabilidade: +1 em uma Jogada de Proteção à escolha."
        ]
        self.peso_base = 80.0
