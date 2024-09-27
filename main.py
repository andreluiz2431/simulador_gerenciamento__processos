import random
import time
from simulacao import SimulacaoProcessos

class Processo:
    def __init__(self, id, tempo_execucao, prioridade=0):
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.tempo_restante = tempo_execucao
        self.estado = 'Pronto'  # Estados: 'Pronto', 'Executando', 'Bloqueado', 'Finalizado'
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

    def criar_processo(self, tempo_execucao, prioridade=0):
        novo_processo = Processo(len(self.fila_processos), tempo_execucao, prioridade)
        self.fila_processos.append(novo_processo)

    def exibir_status(self):
        print("\n=== Status dos Processos ===")
        for processo in self.fila_processos:
            print(f"Processo {processo.id} | Estado: {processo.estado} | Tempo Restante: {processo.tempo_restante} | Prioridade: {processo.prioridade}")
        print("============================\n")

    def escalonar_fifo(self):
        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()
            
            # Simulando execução completa do processo
            while processo_atual.tempo_restante > 0:
                self.exibir_status()  # Exibir o status a cada ciclo
                time.sleep(1)  # Simula o tempo de execução
                processo_atual.tempo_restante -= 1
            
            processo_atual.finalizar()
            self.processos_finalizados.append(processo_atual)
            print(f"Processo {processo_atual.id} finalizado.")

    def escalonar_round_robin(self, quantum):
        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()
            
            # Simulando execução limitada pelo quantum
            for _ in range(quantum):
                if processo_atual.tempo_restante > 0:
                    self.exibir_status()  # Exibir o status a cada ciclo
                    time.sleep(1)  # Simula o tempo de execução
                    processo_atual.tempo_restante -= 1
                else:
                    break

            if processo_atual.tempo_restante > 0:
                processo_atual.pronto()  # Reenfileirar o processo
                self.fila_processos.append(processo_atual)
            else:
                processo_atual.finalizar()
                self.processos_finalizados.append(processo_atual)
                print(f"Processo {processo_atual.id} finalizado.")

    def escalonar_sjf(self):
        self.fila_processos.sort(key=lambda p: p.tempo_execucao)  # Ordenar por menor tempo de execução

        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()
            
            while processo_atual.tempo_restante > 0:
                self.exibir_status()  # Exibir o status a cada ciclo
                time.sleep(1)  # Simula o tempo de execução
                processo_atual.tempo_restante -= 1

            processo_atual.finalizar()
            self.processos_finalizados.append(processo_atual)
            print(f"Processo {processo_atual.id} finalizado.")

    def escalonar_prioridade(self):
        self.fila_processos.sort(key=lambda p: p.prioridade)  # Ordenar por prioridade (menor valor é mais prioritário)

        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()

            while processo_atual.tempo_restante > 0:
                self.exibir_status()  # Exibir o status a cada ciclo
                time.sleep(1)  # Simula o tempo de execução
                processo_atual.tempo_restante -= 1

            processo_atual.finalizar()
            self.processos_finalizados.append(processo_atual)
            print(f"Processo {processo_atual.id} finalizado.")

    def escalonar_com_bloqueio(self):
        while self.fila_processos:
            processo_atual = self.fila_processos.pop(0)
            processo_atual.iniciar()

            while processo_atual.tempo_restante > 0:
                if random.choice([True, False]):  # Aleatoriamente bloqueia o processo
                    processo_atual.bloquear()
                    self.fila_processos.append(processo_atual)  # Reenfileirar o processo bloqueado
                    print(f"Processo {processo_atual.id} foi bloqueado e reenfileirado.")
                    break
                self.exibir_status()  # Exibir o status a cada ciclo
                time.sleep(1)  # Simula o tempo de execução
                processo_atual.tempo_restante -= 1

            if processo_atual.estado != 'Bloqueado':
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

if __name__ == "__main__":
    simulacao = SimulacaoProcessos()
    simulacao.iniciar_simulacao()
