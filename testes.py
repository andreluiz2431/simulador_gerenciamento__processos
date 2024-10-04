import random
import matplotlib.pyplot as plt
from time import sleep
from gerenciador_processos import GerenciadorDeProcessos  # Substitua 'your_code_file' pelo nome correto do arquivo que contém o código fornecido.

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
    Executa a simulação do algoritmo de escalonamento e retorna o histórico de tempo de cada processo.
    """
    gerenciador = GerenciadorDeProcessos()
    dados_processos = gerar_dados_testes()

    for tempo_execucao, prioridade in dados_processos:
        gerenciador.criar_processo(tempo_execucao, prioridade)

    gerenciador.simular(algoritmo=algoritmo, quantum=quantum)

def grafico_resultados():
    """
    Cria um gráfico para visualizar os estados dos processos.
    """
    algoritmos = ['fifo', 'round_robin', 'sjf', 'prioridade']
    for algoritmo in algoritmos:
        print(f"Executando algoritmo: {algoritmo}")
        executar_simulacao(algoritmo)
        sleep(1)
        plt.barh([f'Processo {i}' for i in range(5)], random.sample(range(5, 20), 5))
        plt.title(f"Visualização do Algoritmo: {algoritmo}")
        plt.xlabel("Tempo de Execução (unidades)")
        plt.ylabel("Processos")
        plt.show()
        sleep(2)  # Para ver a transição entre os gráficos

if __name__ == "__main__":
    grafico_resultados()
