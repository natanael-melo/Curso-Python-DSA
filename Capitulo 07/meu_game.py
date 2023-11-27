# Import
import random
from os import system, name


# Função para limpar a tela
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Função para imprimir o menu na tela
def menu():

    print('\n\t***** OPÇÕES *****')
    print('\t1 - Frutas')
    print('\t2 - Pais')
    print('\t3 - Objeto')
    print('\t4 - Cor')
    print('\t5 - Aleatorio')

# Função para selecionar aleatoriamente uma palavra
def selecionar_palavra(opcao):

    # Categorias de palavras
    fruta = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    pais = ['brasil', 'chile', 'alemanha', 'inglaterra', 'portugual']
    objeto = ['cama', 'alicate', 'chuveiro', 'cadeira', 'janela']
    cor = ['amarelo', 'laranja', 'verde', 'azul', 'rosa']

    categorias = [fruta, pais, objeto, cor]

    match opcao:
        case 1:
            palavra = random.choice(fruta).upper()
            return palavra
        case 2:
            palavra = random.choice(pais).upper()
            return palavra
        case 3:
            palavra = random.choice(objeto).upper()
            return palavra
        case 4:
            palavra = random.choice(cor).upper()
            return palavra
        case 5:
            palavra = random.choice(random.choice(categorias)).upper()
            return palavra

# Função para realizar e verificar uma tentativa do usuário
def verificar_tentativa(palavra, chances, letras_descobertas, letras_erradas):

    while True:
        # Ler a tentativa do usuário
        tentativa = str(input('Quer tentar qual letra: ')).upper()

        # Verifica se a tentativa já foi adivinha dentre as descobertas
        if tentativa in letras_descobertas:
            print('\nVocê já tentou essa letra!')
            print('Tente outra letra...\n')

        # Verifica se a tentativa está na palavra
        elif tentativa in palavra:
            index = 0

            # Se estiver, identificar qual o index e substituir
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = tentativa

                index += 1

            return chances, letras_descobertas, letras_erradas

        # Verifica se a tentativa já foi realizada dentre as erradas
        elif tentativa in letras_erradas:
            print('\nVocê já tentou essa letra!')
            print('Tente outra letra...\n')

        # Verifica se a tentativa não está na palavra enquanto ele ainda tem chances
        elif (tentativa not in palavra) and (chances > 0):
            print('\nVocê errou a letra! Tente de novo!')
            letras_erradas.append(tentativa)
            chances -= 1
            return chances, letras_descobertas, letras_erradas

# Função do game
def game():

    # Limpa a tela
    limpa_tela()

    # Mensagens de boas vindas
    print("\nBem vindo ao jogo da forca!")
    print("Escolha uma categoria:")

    # Imprimir o menu
    menu()

    # Usuário seleciona a opção
    op = int(input('\nEai, qual opção será (1/2/3/4/5): '))

    # Palavra é selecionada aleatoriamente
    palavra = selecionar_palavra(op)

    # Lista para amazernar as letras da palavra.
    letras_descobertas = ['_' for letra in palavra]  # Cada letra na palavra recebe '_'

    # Lista para letras erradas
    letras_erradas = []

    # Número de chances que o usuário tem
    chances = 6

    # Looping para tentatovas
    while chances > 0:

        print('\nQual palavra é essa?')
        print(' '.join(letras_descobertas))
        print(f'\nVocê tem {chances} tentativas para acertar!')
        if len(letras_erradas) != 0:
            print('Você já tentou as letras: ', ' '.join(letras_erradas))

        # Tentativas do usuário
        chances, letras_descobertas, letras_erradas = verificar_tentativa(palavra, chances, letras_descobertas, letras_erradas)

        # Mensagem caso o usuário acerte todas as letras
        if '_' not in letras_descobertas:
            print('\nParabéns, você acerto todas as letras!')
            print('A palavra era...')
            print(' '.join(letras_descobertas))
            break

        # Limpa a tela
        limpa_tela()

    # Mensagem caso o usuário não acerte a palavra
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra.upper())

# Função para continuar jogando
def continua():

    while True:
        op = str(input('\nDeseja tentar outra palavra (S/N): ')).upper()

        if op == 'S':
            return op

        elif op == 'N':
            return op

        else:
            print('Opção Invalida! Tente novamente')


while True:

    # Inicia o game
    game()

    # Mensagem para saber se deseja continuar jogando
    flag = continua()

    # Se o usuário quiser sair
    if flag == 'N':
        break
