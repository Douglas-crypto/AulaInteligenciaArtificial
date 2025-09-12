# ClassAmbiente.py
class Ambiente:
    def __init__(self, posicao = 10):  
        self.estado = ["sujo", "limpo", "sujo", "X", "sujo",
                       "limpo", "sujo", "limpo", "X", "sujo"]

    def mostrar_ambiente(self):
        for i, estado in enumerate(self.estado):
            print(f"Posição {i}: {estado}")     