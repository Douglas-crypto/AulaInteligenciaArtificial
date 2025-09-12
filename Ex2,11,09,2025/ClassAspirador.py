import random

class Aspirador:
    def __init__(self, posicao= 0, energia = 20):
        self.posicao = posicao
        self.visitados = []
        self.energia = energia

    def perceber(self, ambiente):
        return ambiente.estado[self.posicao]
    
    def agir(self, ambiente):
        if self.energia <= 0:
            print("Energia esgotada!.")
            return False
        
        percepcao = self.perceber(ambiente)

        if self.posicao in self.visitados:
            print("Movendo para proxima posição")

        else:
            self.visitados.append(self.posicao)

        if percepcao == "sujo":
            ambiente.estado[self.posicao] = "limpo"
            print(f"[Energia: {self.energia}] Limpando posição {self.posicao}")

        elif percepcao == "limpo":
            print(f"[Energia: {self.energia}] Posição {self.posicao} já limpa, movendo...") 
        
        elif percepcao == "X":
            print(f"[Energia: {self.energia}] Obstaculo na posição {self.posicao}, mudando direção...")

        else:
            print("Não se pode ir para essa posição")

        self.energia -= 1
        return True
            


    def mover(self, ambiente):
        if self.energia <= 0:
            return
        
        direcoes = ["direita", "esquerda"]
        random.shuffle(direcoes)
        

        for direcao in direcoes:
            if direcao == "direita":
                if self.posicao + 1 < len(ambiente.estado) and ambiente.estado[self.posicao + 1] != "X":
                    self.posicao += 1
                    print(f"Movendo para direita -> posição {self.posicao}")
                    self.energia -= 1
                    return
                
            elif direcao == "esquerda":
                    if self.posicao - 1 >= 0 and ambiente.estado[self.posicao - 1] != "X":
                        self.posicao -= 1
                        print(f"Movendo para esquerda -> posição {self.posicao}")
                        self.energia -= 1
                        return
                    
        print(" Nenhum movimento possível existe um obstaculo em ambas as direções.")
        self.energia -= 1