import random
import matplotlib.pyplot as plt
from time import time
from your_code_file import GerenciadorDeProcessos  # Substitua pelo arquivo onde está seu código de escalonamento

def gerar_dados_testes():
    """
    Gera um conjunto de processos aleatórios para testes.
    """
    processos = []
    for _ in range(5):
        tempo_execucao = random.randint(2, 10)
        prioridade = random.randint(1, 5)
        processos.append((tempo_execucao, prioridade))
    return processos

def executar_simulacao(algoritmo, quantum=2):
    """
    Executa a simulação e calcula o tempo total de execução do algoritmo.
    """
    gerenciador = GerenciadorDeProcessos()
    dados_processos = gerar_dados_testes()

    for tempo_execucao, prioridade in dados_processos:
        gerenciador.criar_processo(tempo_execucao, prioridade)

    inicio = time()
    gerenciador.simular(algoritmo=algoritmo, quantum=quantum)
    fim = time()

    return fim - inicio

def comparar_algoritmos():
    """
    Compara os tempos de execução dos diferentes algoritmos.
    """
    algoritmos = ['fifo', 'round_robin', 'sjf', 'prioridade']
    tempos_execucao = []

    for algoritmo in algoritmos:
        print(f"Executando algoritmo: {algoritmo}")
        tempo_execucao = executar_simulacao(algoritmo)
        tempos_execucao.append(tempo_execucao)

    # Exibir os tempos de execução em um gráfico
    plt.bar(algoritmos, tempos_execucao, color=['blue', 'green', 'red', 'purple'])
    plt.title('Comparação dos Tempos de Execução por Algoritmo')
    plt.xlabel('Algoritmo')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.show()

if __name__ == "__main__":
    comparar_algoritmos()
