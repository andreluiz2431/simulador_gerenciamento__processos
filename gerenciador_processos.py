import random

class Processo:
    def __init__(self, id, tempo_execucao, prioridade=0):
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
        self.fila_processos = []
        self.processos_finalizados = []
        self.tempo_atual = 0

    def criar_processo(self, tempo_execucao, prioridade=0):
        novo_processo = Processo(len(self.fila_processos), tempo_execucao, prioridade)
        self.fila_processos.append(novo_processo)

    def exibir_estados_processos(self):
        print(f"=== Tempo: {self.tempo_atual} ===")
        for processo in self.fila_processos:
            print(f"Processo {processo.id}: {processo.estado}, Tempo restante: {processo.tempo_restante}")
        print()

    def escalonar_fifo(self):
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
        if algoritmo == 'fifo':
            self.escalonar_fifo()
        elif algoritmo == 'round_robin':
            self.escalonar_round_robin(quantum)
        elif algoritmo == 'sjf':
            self.escalonar_sjf()
        elif algoritmo == 'prioridade':
            self.escalonar_prioridade()
