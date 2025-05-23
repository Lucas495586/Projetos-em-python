import random

def jogo():
    dificuldade = int(input('Escolha a dificuldade: 1 - Fácil, 2 - Médio, 3 - Difícil: '))

    if dificuldade == 1:
        tentativas = 10
        print('Fácil')
    elif dificuldade == 2:
        tentativas = 6
        print('Médio')
    elif dificuldade == 3:
        tentativas = 3
        print('Difícil')
    else:
        print("Opção inválida.")
        return 0
    
    numero_secreto = random.randint(1, 100)

    whil(tentativas <= 0):

 