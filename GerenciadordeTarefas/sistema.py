from GerenciadordeTarefas.biblioteca.arquivo import *
from GerenciadordeTarefas.biblioteca.interface import *
from time import sleep

arquivo = 'Tarefas.txt'
if not arquivoexiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Criar tarefa', 'Listar Tarefas', 'Marcar tarefa como concluida', 'Remover Tarefa', 'Sair do sistema'])
    if resposta == 1:
        header('NOVA TAREFA')
        nome = str(input('Digite o a tarefa: '))
        estado = str(input('Digite o estado da sua tarefa: (concluida / em execução / pendente)'))
        criarTarefa(arquivo, nome, estado)
    elif resposta == 2:
        listarTarefas(arquivo)
    elif resposta == 3:
        nome = str(input('Digite o nome da tarefa que deseja marcar como concluída: '))
        marcarConcluida(arquivo, nome)
    elif resposta == 4:
        tarefa = str(input('Digite a tarefa que deseja remover: '))
        removerTarefa(arquivo, tarefa)
    elif resposta == 5:
        print('\033[31mSaindo do sistema...\033[m')
        break
    else:
        print('\033[31mERRO!\033[m Valor inválido digitado!')