import random

def jogo():
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.\n")

    dificuldade = int(input('Escolha a dificuldade: 1 - Fácil, 2 - Médio, 3 - Difícil: '))

    if dificuldade == 1:
        tentativas = 10
        print('Dificuldade: Fácil')
    elif dificuldade == 2:
        tentativas = 6
        print('Dificuldade: Médio')
    elif dificuldade == 3:
        tentativas = 3
        print('Dificuldade: Difícil')
    else:
        print("Opção inválida.")
        return

    numero_secreto = random.randint(1, 100)

    while tentativas > 0:
        print(f'\nVocê tem {tentativas} tentativa(s) restante(s).')
        try:
            palpite = int(input('Digite seu palpite: '))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if palpite < 1 or palpite > 100:
            print("Seu palpite deve ser entre 1 e 100.")
            continue

        if palpite == numero_secreto:
            print(f'🎉 Parabéns! Você acertou o número {numero_secreto}!')
            break
        elif palpite < numero_secreto:
            print('O número é **MAIOR** que isso.')
        else:
            print('O número é **MENOR** que isso.')

        tentativas -= 1

    if tentativas == 0:
        print(f'\n💀 Suas tentativas acabaram. O número era {numero_secreto}. Tente novamente!')

# Executar o jogo
if __name__ == "__main__":
    jogo()