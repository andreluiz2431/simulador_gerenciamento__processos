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
        # Implementar FIFO
        pass

    def escalonar_round_robin(self, quantum):
        # Implementar Round-Robin
        pass

    def escalonar_sjf(self):
        # Implementar Shortest Job First
        pass

    def escalonar_prioridade(self):
        # Implementar escalonamento por prioridade
        pass

    def simular(self):
        # Simular a execução e escalonamento dos processos
        pass
