# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************\n")

while True:

    # Menu
    print('\n\t***** OPÇÕES *****')
    print('\t1 - Somar')
    print('\t2 - Subtrair')
    print('\t3 - Multiplicar')
    print('\t4 - Dividir')
    print('\t5 - Desligar')

    op = int(input('\nDigite uma das opções acima (1/2/3/4/5): '))

    if op == 5:
        print('\n******************* Desligando Calculadora *******************')
        print('\n******************* Calculadora Desligada *******************')
        break

    x1 = int(input('\nDigite o primeiro número: '))
    x2 = int(input('Digite o primeiro número: '))

    match op:
        case 1:
            r = x1 + x2
            print(f'\n\t{x1} + {x2} = {r}')

        case 2:
            r = x1 - x2
            print(f'\n\t{x1} - {x2} = {r}')

        case 3:
            r = x1 * x2
            print(f'\n\t{x1} * {x2} = {r}')

        case 4:
            r = x1 / x2
            print(f'\n\t{x1} / {x2} = {r}')

    flag = str(input('\nDeseja realizar uma nova conta (S/N): ')).upper()

    if flag == 'N':
        break
