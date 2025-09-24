from .raca import Raca

class Anao(Raca):
    def __init__(self):
        super().__init__()
        self.alinhamento = "Ordem"
        self.infravisao = "18 metros"
        self.movimento = 6
        self.habilidades_raca = [
            "Mineradores: detectar anomalias em pedras.",
            "Vigoroso: +1 em JPC (Constituição).",
            "Restrição de Armas: Não podem usar armas grandes.",
            "Inimigos Naturais: Ataques fáceis contra orcs, ogros e hobgoblins."
        ]
        self.peso_base = 75.0
