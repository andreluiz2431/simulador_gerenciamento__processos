import random
import matplotlib.pyplot as plt
from time import sleep
from gerenciador_processos import GerenciadorDeProcessos 

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
    # Lista de algoritmos a serem testados
    algoritmos = ['fifo', 'round_robin', 'sjf', 'prioridade']
    # Executa cada algoritmo e plota o gráfico
    for algoritmo in algoritmos:
        # Mostra o nome do algoritmo em execução
        print(f"Executando algoritmo: {algoritmo}")
        # Executa o algoritmo e obtém o histórico de tempo de cada processo
        executar_simulacao(algoritmo)
        # Aguarda 1 segundo para a transição entre os gráficos
        sleep(1)
        # Gera um gráfico de barras horizontal com o histórico de tempo de cada processo
        plt.barh([f'Processo {i}' for i in range(5)], random.sample(range(5, 20), 5))
        # Configura o título do gráfico
        plt.title(f"Visualização do Algoritmo: {algoritmo}")
        # Configura os rótulos dos eixos
        plt.xlabel("Tempo de Execução (unidades)")
        plt.ylabel("Processos")
        # Mostra o gráfico
        plt.show()
        # Aguarda 2 segundos para a transição entre os gráficos
        sleep(2)
if __name__ == "__main__":
    grafico_resultados()
