from gerenciador_processos import GerenciadorDeProcessos
import random

class SimulacaoProcessos:
    def __init__(self):
        self.gerenciador = GerenciadorDeProcessos()

    def iniciar_simulacao(self):
        print("=== Simulação de Gerenciamento de Processos ===")
        
        algoritmos_validos = ['fifo', 'round_robin', 'sjf', 'prioridade']
        algoritmo = input(f"Escolha o algoritmo de escalonamento {algoritmos_validos}: ").strip().lower()

        while algoritmo not in algoritmos_validos:
            print("Algoritmo inválido. Tente novamente.")
            algoritmo = input(f"Escolha o algoritmo de escalonamento {algoritmos_validos}: ").strip().lower()

        if algoritmo == 'round_robin':
            quantum = int(input("Digite o valor do quantum para Round Robin: "))
        else:
            quantum = 2

        num_processos = int(input("Quantos processos deseja simular? "))

        for i in range(num_processos):
            tempo_execucao = random.randint(1, 10)
            prioridade = random.randint(1, 5)
            self.gerenciador.criar_processo(tempo_execucao, prioridade)

        print(f"{num_processos} processos foram criados.\nIniciando a simulação...\n")

        self.gerenciador.simular(algoritmo, quantum)

        print("Simulação finalizada!")
