from GerenciadordeTarefas.biblioteca.interface import *

def arquivoexiste(nome):
    """
    Verifica se o arquivo existe no diretório
    :param nome: nome ou caminho do arquivo
    :return: True se existir, caso contrário, False
    """
    try:
        abrir =open(nome, 'rt')
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    """
    Cria um novo arquivo vazio

    :param nome: Nome que será dado ao arquivo criado
    """

    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um \033[31mERRO\033[m na criação de arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def criarTarefa(arquivo, nome = 'Tarefa 1', estado = 'pendente'):
    """
    Adiciona uma nova tarefa ao arquivo

    :param arquivo: onde as tarefas serão armazenadas
    :param nome: nome da tarefa
    :param estado: estado inicial em que se encontra a tarefa (pendente/em execução/concluida)
    """
    try:
        abrir = open(arquivo, 'at', encoding='utf-8')
    except:
        print('Houve um \033[31mERRO\033[m na abertura do arquivo!')
    else:
        try:
            abrir.write(f'{nome};{estado}\n')
        except:
            print('\033[31mERRO\033[m ao escrever os dados')
        else:
            print(f'Nova tarefa {nome} adicionada')
            abrir.close()


def removerTarefa(arquivo, tarefa):
    """
    Remove uma tarefa do arquivo, caso ele exista

    :param arquivo: arquivo com as tarefas
    :param tarefa:  nome da tarefa que será removida
    """
    temporarias = []
    removida = False

    try:
        with open(arquivo, 'r') as abrir:
            for linha in abrir:
                nome = linha.strip().split(';')[0]
                if nome != tarefa:
                    temporarias.append(linha)
                else:
                    removida = True
    except OSError:
        print('\033[31mERRO\033[m ao abrir arquivo!')
        return

    try:
        with open(arquivo, 'w') as abrir:
            abrir.writelines(temporarias)
    except OSError:
        print('\033[31mERRO\033[m ao apagar tarefa')
        return

    if removida:
        print(f'Tarefa "{tarefa}" apagada com sucesso!')
    else:
        print(f'Tarefa "{tarefa}" não encontrada.')

def listarTarefas(nome):
    """
    Lista todas as tarefas armazendas no arquivo

    :param nome: arquivo de tarefas
    """
    try:
        abrir = open(nome, 'rt')
    except:
        print('\033[31mERRO\033[m ao ler arquivo!')
    else:
        header('LISTA DE TAREFAS')
        for linha in abrir:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<5}, estado da tarefa: {dado[1]:>3}')
    finally:
        abrir.close()


def marcarConcluida(arquivo, nome):
    """
    Muda o estado de uma tarefa para concluida, caso ela exista ou já não esteja concluida

    :param arquivo: arquivo de tarefas
    :param nome: nome da tarefa a ser marcada
    """
    tarefas = []
    encontrada = False

    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                tarefa, estado = linha.strip().split(';')

                if tarefa == nome:
                    encontrada = True
                    if estado == 'concluida':
                        print('Esta tarefa já está concluída!')
                        tarefas.append(linha)
                    else:
                        tarefas.append(f'{tarefa};concluida\n')
                        print('Tarefa marcada como concluída!')
                else:
                    tarefas.append(linha)

    except OSError:
        print('\033[31mERRO\033[m ao abrir arquivo!')
        return

    if not encontrada:
        print('Esta tarefa não existe!')
        return

    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.writelines(tarefas)
    except OSError:
        print('\033[31mERRO\033[m ao salvar alterações!')
