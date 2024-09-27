class Processo:
    def __init__(self, id, tempo_execucao, prioridade=0):
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.tempo_restante = tempo_execucao
        self.estado = 'Pronto'  # 'Executando', 'Bloqueado', 'Finalizado'
        self.prioridade = prioridade

    def iniciar(self):
        self.estado = 'Executando'

    def bloquear(self):
        self.estado = 'Bloqueado'

    def finalizar(self):
        self.estado = 'Finalizado'

class GerenciadorDeProcessos:
    def __init__(self):
        self.fila_processos = []
        self.processos_finalizados = []

    def criar_processo(self, tempo_execucao, prioridade=0):
        novo_processo = Processo(len(self.fila_processos), tempo_execucao, prioridade)
        self.fila_processos.append(novo_processo)

    def escalonar_fifo(self):
        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()
            
            # Simulando execução completa do processo
            while processo_atual.tempo_restante > 0:
                processo_atual.tempo_restante -= 1
            
            processo_atual.finalizar()
            self.processos_finalizados.append(processo_atual)
            print(f"Processo {processo_atual.id} finalizado.")

    def escalonar_round_robin(self, quantum):
        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()
            
            # Simulando execução limitada pelo quantum
            if processo_atual.tempo_restante > quantum:
                processo_atual.tempo_restante -= quantum
                self.fila_processos.append(processo_atual)  # Reenfileirar o processo
            else:
                processo_atual.tempo_restante = 0
                processo_atual.finalizar()
                self.processos_finalizados.append(processo_atual)
                print(f"Processo {processo_atual.id} finalizado.")

    def escalonar_sjf(self):
        # Ordenar a fila de processos com base no tempo de execução
        self.fila_processos.sort(key=lambda p: p.tempo_execucao)

        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()
            
            # Simulando execução completa do processo
            while processo_atual.tempo_restante > 0:
                processo_atual.tempo_restante -= 1
            
            processo_atual.finalizar()
            self.processos_finalizados.append(processo_atual)
            print(f"Processo {processo_atual.id} finalizado.")

    def escalonar_prioridade(self):
        # Ordenar a fila de processos com base na prioridade
        self.fila_processos.sort(key=lambda p: p.prioridade)

        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()
            
            # Simulando execução completa do processo
            while processo_atual.tempo_restante > 0:
                processo_atual.tempo_restante -= 1
            
            processo_atual.finalizar()
            self.processos_finalizados.append(processo_atual)
            print(f"Processo {processo_atual.id} finalizado.")

    def simular(self, algoritmo='fifo', quantum=2):
        if algoritmo == 'fifo':
            self.escalonar_fifo()
        elif algoritmo == 'round_robin':
            self.escalonar_round_robin(quantum)
        elif algoritmo == 'sjf':
            self.escalonar_sjf()
        elif algoritmo == 'prioridade':
            self.escalonar_prioridade()
