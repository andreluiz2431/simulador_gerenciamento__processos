A arquitetura da simulação

1. Modelo de Processos
Classe Processo: cada processo terá atributos como ID, tempo de execução, tempo restante, estado (Pronto, Executando, Bloqueado, Finalizado), e prioridade (se aplicável).
Métodos que alteram o estado do processo, como iniciar(), bloquear(), finalizar(), etc.

2. Gerenciador de Processos
Classe GerenciadorDeProcessos: será responsável por criar, gerenciar e monitorar os processos. Deve incluir:
Fila de Processos: armazena os processos que aguardam execução.
Algoritmos de Escalonamento: Implementar FIFO, Round-Robin, SJF e Prioridade como métodos separados.
Troca de Contexto: simular a troca de processos entre o estado de execução e pronto.

3. Interface da Simulação
Interface de Linha de Comando (CLI) ou Interface Gráfica (GUI):
Exibir o estado dos processos, tempos de execução, e eventos de escalonamento.
Atualizar dinamicamente conforme os processos são escalonados e executados.