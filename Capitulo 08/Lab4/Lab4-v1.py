# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import name, system


# Função para limpar a tela
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# Board (tabuleiro)
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
def imprimir_game_status():
    print()


class Hangman:

    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_descobertas = []

    # Método para adivinhar a letra
    def verificar_tentativa(self, letra):
        if letra in self.palavra and letra not in self.letras_descobertas:
            self.letras_descobertas.append(letra)

        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)

        else:
            return False

        return True

    # Método para não mostrar a letra no board
    def esconder_letra(self):

        palavra = ''

        for letra in self.palavra:
            if letra not in self.letras_descobertas:
                palavra += '_'
            else:
                palavra += letra
        return palavra

    # Método para verificar se o jogador venceu
    def usuario_ganhou(self):
        if '-' not in self.esconder_letra():
            return True
        return False

    # Método para verificar se o jogo terminou
    def usuario_perdeu(self):
        return self.usuario_ganhou() or (len(self.letras_erradas) == 6)

    # Método para checar o status do game e imprimir o board na tela
    def imprimir_game_status(self):
        limpa_tela()

        print(board[len(self.letras_erradas)])

        print('Palavra: ' + self.esconder_letra())

        print(f'Letras Usadas: {self.letras_erradas}')


def menu():
    print('\n\t***** OPÇÕES *****')
    print('\t1 - Frutas')
    print('\t2 - Pais')
    print('\t3 - Objeto')
    print('\t4 - Cor')
    print('\t5 - Aleatorio')


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
    jogo = Hangman(selecionar_palavra(op))

    # Looping para tentatovas
    while not jogo.usuario_ganhou():

        jogo.imprimir_game_status()

        print('\nQual palavra é essa?')

        letra = str(input('Chute uma letra: '))

        jogo.verificar_tentativa(letra)

    if jogo.usuario_ganhou():
        print('\nParabéns, você acerto todas as letras!')
        print('A palavra era...')
        print(jogo.palavra)
    else:
        print('\nGame over! Você perdeu!')
        print('A palavra era...')
        print(jogo.palavra)

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
