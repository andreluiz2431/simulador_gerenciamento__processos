https://www.dcce.ibilce.unesp.br/~aleardo/cursos/fsc/cap03.php#:~:text=Em%20espera%20(ou%20bloqueado)%2C,)%2C%20quando%20não%20estiver%20executando.

# FAZER
- ✅ No início não deixar todos os processos de prontidão, largar aos poucos, exemplo: FIFO, 30 processos, random(0, 5) processos Prontos para executar, da um tempo e larga mais random(0, 5) processos Prontos para executar.
- ✅ Fila de processos desbloqueados não podem estar separados da fila de processos, quendo desbloqueado alocar o mesmo de volta a fila de processos prontos.
- Trabalhar com valores fixos em vez de aleatórios afim de testar e debugar em todo o código (tempo de execução de cada processo, tempo de bloqueio, quantidade de processos prontos para executar)



# Simulador de Gerenciamento de Processos

## Introdução
Este projeto é um simulador de gerenciamento de processos que implementa diferentes algoritmos de escalonamento de processos, incluindo FIFO (First In, First Out), Round Robin, SJF (Shortest Job First) e Prioridade. O simulador permite a criação de processos com tempos de execução e prioridades aleatórios, e simula a execução desses processos com base no algoritmo de escalonamento escolhido.

## Estrutura do Projeto
O projeto consiste em três arquivos principais:

- gerenciador_processos.py: Contém as definições das classes e funções responsáveis pela gestão dos processos e pela implementação dos algoritmos de escalonamento.
- main.py: O ponto de entrada do programa, que inicia a simulação.
- simulacao.py: Contém a lógica para iniciar a simulação e interagir com o usuário.

## Arquivo: gerenciador_processos.py
### Importações
import random

- random: Para gerar números aleatórios, utilizados na criação dos tempos de execução e prioridades dos processos.

### Classe: Processo
Esta classe representa um processo que será gerenciado pelo simulador.

Atributos:
- id: Identificador único do processo.
- tempo_execucao: Tempo total necessário para executar o processo.
- tempo_restante: Tempo restante para concluir a execução.
- estado: Estado atual do processo (Pronto, Executando, Bloqueado, Finalizado).
- prioridade: Prioridade do processo.

Métodos:
- __init__(self, id, tempo_execucao, prioridade=0): Construtor da classe, inicializa um novo processo.
- iniciar(self): Muda o estado do processo para 'Executando' e imprime uma mensagem.
- bloquear(self): Muda o estado do processo para 'Bloqueado' e imprime uma mensagem.
- desbloquear(self): Muda o estado do processo para 'Desbloqueado' e imprime uma mensagem.
- finalizar(self): Muda o estado do processo para 'Finalizado' e imprime uma mensagem.
- pronto(self): Muda o estado do processo para 'Pronto' e imprime uma mensagem.

### Classe: GerenciadorDeProcessos
Esta classe gerencia a criação e o escalonamento dos processos.

Atributos:
- fila_processos: Lista que armazena os processos em execução.
- processos_finalizados: Lista que armazena os processos que foram finalizados.

Métodos:
- __init__(self): Construtor da classe, inicializa a fila de processos e a lista de processos finalizados.
- criar_processo(self, tempo_execucao, prioridade=0): Cria um novo processo e o adiciona à fila de processos.
- exibir_estados_processos(): Exibe os processos e seus dados
- exibir_estados_processos_barra(): Exibe os processos e seus dados com barra de estimativa de tempo
- executar_processos(self): Percorre e executa o processo
- escalonar_fifo(self): Implementa o algoritmo FIFO para escalonamento de processos.
Remove o primeiro processo da fila, inicia sua execução até que seu tempo restante seja 0 e finaliza o processo, armazenando-o na lista de finalizados.
- escalonar_round_robin(self, quantum): Implementa o algoritmo Round Robin para escalonamento de processos.
Remove o primeiro processo da fila, inicia sua execução e permite que ele execute por um tempo máximo definido pelo quantum. Se o tempo restante for maior que o quantum, o processo é colocado de volta na fila. Caso contrário, o processo é finalizado.
- escalonar_sjf(self): Implementa o algoritmo SJF (Shortest Job First).
Ordena a fila de processos pelo tempo de execução e executa cada processo até que seu tempo restante seja 0, finalizando-o.
- escalonar_prioridade(self): Implementa o algoritmo de escalonamento por prioridade.
Ordena a fila de processos pela prioridade e executa cada processo até que seu tempo restante seja 0, finalizando-o.
- simular(self, algoritmo='fifo', quantum=2): Método principal que inicia a simulação com base no algoritmo escolhido e no valor do quantum. Chama o método correspondente ao algoritmo.

## Arquivo: main.py
from simulacao import SimulacaoProcessos

Este arquivo é o ponto de entrada do programa. Ele importa a classe SimulacaoProcessos do arquivo simulacao.py e inicia a simulação ao chamar iniciar_simulacao().

## Arquivo: simulacao.py
### Importações
from gerenciador_processos import GerenciadorDeProcessos

import random

- Importa a classe GerenciadorDeProcessos para gerenciar os processos e gera números aleatórios.

### Classe: SimulacaoProcessos
Esta classe controla o fluxo da simulação e interage com o usuário.

Atributos:
- gerenciador: Uma instância da classe GerenciadorDeProcessos.

Métodos:
- __init__(self): Construtor da classe que inicializa o gerenciador de processos.
- iniciar_simulacao(self): Método principal que gerencia a simulação.
Solicita ao usuário que escolha um algoritmo de escalonamento e, se necessário, o valor do quantum.
Solicita o número de processos a serem simulados e cria processos com tempos de execução e prioridades aleatórios.
Inicia a simulação chamando o método simular() do gerenciador.

## Conclusão
O simulador de gerenciamento de processos fornece uma forma prática de entender como diferentes algoritmos de escalonamento funcionam na prática. Com uma interface simples e clara, o usuário pode observar a execução dos processos e como cada algoritmo gerencia a fila de processos com base em seus tempos de execução e prioridades.
