import random

class Processo:
    def __init__(self, id, tempo_execucao, prioridade=0):
        """
        Construtor da classe Processo.

        Args:
            id (int): Identificador do processo.
            tempo_execucao (int): Tempo total necessário para executar o processo.
            prioridade (int, optional): Prioridade do processo. Defaults to 0.
        """
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.tempo_restante = tempo_execucao
        self.estado = 'Pronto'
        self.prioridade = prioridade

    def iniciar(self):
        self.estado = 'Executando'
        print(f"Processo {self.id} está em execução.")

    def bloquear(self):
        self.estado = 'Bloqueado'
        print(f"Processo {self.id} foi bloqueado.")

    def finalizar(self):
        self.estado = 'Finalizado'
        print(f"Processo {self.id} foi finalizado.")
    
    def pronto(self):
        self.estado = 'Pronto'
        print(f"Processo {self.id} está pronto para execução.")

class GerenciadorDeProcessos:
    def __init__(self):
        # Construtor da classe, inicializa a fila de processos e a lista de processos finalizados.
        self.fila_processos = []
        self.processos_finalizados = []
        self.tempo_atual = 0

    def criar_processo(self, tempo_execucao, prioridade=0):
        """
        Cria um novo processo e o adiciona à fila de processos.
        
        Args:
            tempo_execucao (int): Tempo total necessário para executar o processo.
            prioridade (int, optional): Prioridade do processo. Defaults to 0.
        """
        novo_processo = Processo(len(self.fila_processos), tempo_execucao, prioridade)
        self.fila_processos.append(novo_processo)

    def exibir_estados_processos(self):
        """
        Exibe o estado atual dos processos na fila de processos.

        Mostra o tempo atual e o estado de cada processo na fila de processos.
        """
        print(f"=== Tempo: {self.tempo_atual} ===")
        for processo in self.fila_processos:
            print(f"Processo {processo.id}: {processo.estado}, Tempo restante: {processo.tempo_restante}")
        print()

    def escalonar_fifo(self):
        """
        Implementa o algoritmo FIFO para escalonamento de processos.
        Remove o primeiro processo da fila, inicia sua execução até que seu tempo restante seja 0 e finaliza o processo, armazenando-o na lista de finalizados.
        """
        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()
            while processo_atual.tempo_restante > 0:
                self.exibir_estados_processos()
                processo_atual.tempo_restante -= 1
                self.tempo_atual += 1
            processo_atual.finalizar()
            self.processos_finalizados.append(processo_atual)

    def escalonar_round_robin(self, quantum):
        """
        Implementa o algoritmo Round Robin para escalonamento de processos.
        Remove o primeiro processo da fila, inicia sua execução por um tempo máximo definido pelo quantum.
        Se o tempo restante for maior que o quantum, o processo é colocado de volta na fila.
        Caso contrário, o processo é finalizado.
        """
        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()
            tempo_execucao = min(processo_atual.tempo_restante, quantum)
            for _ in range(tempo_execucao):
                self.exibir_estados_processos()
                processo_atual.tempo_restante -= 1
                self.tempo_atual += 1
            
            if processo_atual.tempo_restante > 0:
                processo_atual.pronto()
                self.fila_processos.append(processo_atual)
            else:
                processo_atual.finalizar()
                self.processos_finalizados.append(processo_atual)

    def escalonar_sjf(self):
        """
        Implementa o algoritmo SJF (Shortest Job First) para escalonamento de processos.
        Ordena a fila de processos pelo tempo de execução e executa cada processo até que seu tempo restante seja 0, finalizando-o.
        """
        self.fila_processos.sort(key=lambda p: p.tempo_execucao)
        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()
            while processo_atual.tempo_restante > 0:
                self.exibir_estados_processos()
                processo_atual.tempo_restante -= 1
                self.tempo_atual += 1
            processo_atual.finalizar()
            self.processos_finalizados.append(processo_atual)

    def escalonar_prioridade(self):
        """
        Implementa o algoritmo de escalonamento por prioridade.
        Ordena a fila de processos pela prioridade e executa cada processo até que seu tempo restante seja 0, finalizando-o.
        """        
        self.fila_processos.sort(key=lambda p: p.prioridade)
        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()
            while processo_atual.tempo_restante > 0:
                self.exibir_estados_processos()
                processo_atual.tempo_restante -= 1
                self.tempo_atual += 1
            processo_atual.finalizar()
            self.processos_finalizados.append(processo_atual)

    def simular(self, algoritmo='fifo', quantum=2):
        """
        Simula o escalonamento de processos com base no algoritmo e
        parâmetros fornecidos.

        Args:
            algoritmo (str, optional): Algoritmo de escalonamento a ser usado.
                Defaults to 'fifo'.
            quantum (int, optional): Tempo de execução de cada processo no
                algoritmo Round Robin. Defaults to 2.
        """
        if algoritmo == 'fifo':
            self.escalonar_fifo()
        elif algoritmo == 'round_robin':
            self.escalonar_round_robin(quantum)
        elif algoritmo == 'sjf':
            self.escalonar_sjf()
        elif algoritmo == 'prioridade':
            self.escalonar_prioridade()
