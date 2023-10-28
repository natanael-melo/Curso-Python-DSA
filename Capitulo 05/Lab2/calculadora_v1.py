# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************\n")


def ler_numeros():
    n1 = int(input('\nDigite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    return n1, n2


def somar():
    x1, x2 = ler_numeros()
    r = x1 + x2
    print(f'\n\t{x1} + {x2} = {r}')


def subtrair():
    x1, x2 = ler_numeros()
    r = x1 - x2
    print(f'\n\t{x1} - {x2} = {r}')


def multiplicar():
    x1, x2 = ler_numeros()
    r = x1 * x2
    print(f'\n\t{x1} * {x2} = {r}')


def dividir():
    x1, x2 = ler_numeros()
    r = x1 / x2
    print(f'\n\t{x1} / {x2} = {r}')


def continua():

    while True:
        op = str(input('\nDeseja realizar uma nova conta (S/N): ')).upper()

        if op == 'S':
            return op

        elif op == 'N':
            return op

        else:
            print('Opção Invalida! Tente novamente')

def msg_desliga():
    print('\n******************* Desligando Calculadora *******************')
    print('\n******************* Calculadora Desligada *******************')


while True:

    # Menu
    print('\n\t***** OPÇÕES *****')
    print('\t1 - Somar')
    print('\t2 - Subtrair')
    print('\t3 - Multiplicar')
    print('\t4 - Dividir')
    print('\t5 - Desligar')

    op = int(input('\nDigite uma das opções acima (1/2/3/4/5): '))

    match op:
        case 1:
            somar()

        case 2:
            subtrair()

        case 3:
            multiplicar()

        case 4:
            dividir()

        case 5:
            msg_desliga()
            break

        case _:
            print('\nOpção Invalida!!!')

    flag = continua()

    if flag == 'N':
        msg_desliga()
        break


