class SimulacaoProcessos:
    def __init__(self):
        self.gerenciador = GerenciadorDeProcessos()

    def iniciar_simulacao(self):
        print("=== Simulação de Gerenciamento de Processos ===")
        
        # Solicitar ao usuário o algoritmo de escalonamento
        algoritmo = input("Escolha o algoritmo de escalonamento (fifo, round_robin, sjf, prioridade): ").strip().lower()

        # Se o algoritmo for Round Robin, pedir o quantum
        if algoritmo == 'round_robin':
            quantum = int(input("Digite o valor do quantum para Round Robin: "))
        else:
            quantum = 2  # Valor padrão para evitar erro se não for Round Robin

        # Solicitar ao usuário o número de processos
        num_processos = int(input("Quantos processos deseja simular? "))

        # Criar processos aleatórios
        for i in range(num_processos):
            tempo_execucao = random.randint(1, 10)  # Tempo de execução aleatório entre 1 e 10
            prioridade = random.randint(1, 5)       # Prioridade aleatória entre 1 e 5
            self.gerenciador.criar_processo(tempo_execucao, prioridade)

        print(f"{num_processos} processos foram criados.\nIniciando a simulação...\n")

        # Chamar o método de simulação com base no algoritmo escolhido
        self.gerenciador.simular(algoritmo, quantum)

        print("Simulação finalizada!")
