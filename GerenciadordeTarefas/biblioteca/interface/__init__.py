def leiainteiro(msg):
    
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
    
    return ('-=' * 46)

def header(txt):
    
    print(linha())
    print(txt.center(46))
    print(linha())


def menu(vetor):
    
    header('MENU PRINCIPAL')
    c = 1
    for item in vetor:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opcao = leiainteiro('\033[35mEscolha que ação deseja executar: \033[m')
    return opcao
