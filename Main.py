from collections import deque
import random

tipospacientes = [1, 2, 3, 4, 5]
identificador = ["Raimunda", "João", "David", "Miranda", "Gustavo", "Benado"]
random.shuffle(identificador)  # Embaralha a lista identificador aleatoriamente
fila = {}

def Montar_Filar():
    for i in identificador:
        fila[i] = random.choice(tipospacientes)
    print("Fila original:", fila)
    
Montar_Filar()

def Ordenar_prioridade():
    global dicionario_ordenado
    # Ordenar primeiro pelo tipo de prioridade e depois pela ordem de chegada
    dicionario_ordenado = sorted(fila.items(), key=lambda x: (x[1], identificador.index(x[0])))
    print("Fila ordenada:", dicionario_ordenado)

Ordenar_prioridade()

def simulação():
    tempo = [1, 3, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    random.shuffle(tempo)
    tempo_total = 0
    for i in range(len(dicionario_ordenado)):
        tempo_total += tempo[i]
        print("O Paciente", i, dicionario_ordenado[i], "já pode entrar e levou cerca de", tempo_total, "minutos para ser atendido")
    print("numero total de pacientes:" , len(dicionario_ordenado) , "| O tempo medio de espera:" , tempo_total/len(dicionario_ordenado) , "| A ordem de atendimento foi: ", dicionario_ordenado ,)
simulação()