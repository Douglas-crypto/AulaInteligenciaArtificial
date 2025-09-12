#Main.py
import ClassAmbiente
import ClassAspirador

ambiente = ClassAmbiente.Ambiente()
aspirador = ClassAspirador.Aspirador()

print("Estado inicial do ambiente:")
ambiente.mostrar_ambiente()

print("\n   Início da simulação: ")

while aspirador.energia > 0:
    if not aspirador.agir(ambiente):
        break
    aspirador.mover(ambiente)

print("\n Estado final do ambiente:")
ambiente.mostrar_ambiente()


