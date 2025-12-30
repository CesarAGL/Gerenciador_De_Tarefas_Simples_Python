def leiainteiro(msg):
    """
    Lê um número inteiro do usuário e trata erros, como erros de digitação e interrupção.

    param msg: mensagem exibida para o usuário
    return: número inteiro digitado ou 0 em caso de interrupção da entrada
    """
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO:por favor, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n
def linha(tamanho = 46):
    """
    Retorna uma linha decorativa para a formatação do menu

    param tamanho: tamanho da linha (quantidade de caracteres)
    return: string formatada
    """
    return ('-=' * 46)

def header(txt):
    """
    Exibe um cabeçalho formatado com linhas decorativas

    param txt: texto que será exibido no cabeçalho
    """
    print(linha())
    print(txt.center(46))
    print(linha())


def menu(vetor):
    """
    exibe um menu numerado a partir de uma lista de opções
    e retorna a opção escolhida pelo usuário

    param vetor: lista de opções do menu
    return número que corresponde a opção escolhida
    """
    header('MENU PRINCIPAL')
    c = 1
    for item in vetor:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opcao = leiainteiro('\033[35mEscolha que ação deseja executar: \033[m')
    return opcao
