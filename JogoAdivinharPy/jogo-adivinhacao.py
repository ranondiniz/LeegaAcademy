import random

def obter_dificuldade():
    while True:
        dificuldade = input("\nEscolha sua dificuldade:\n1. Fácil\n2. Médio\n3. Difícil\nEscolha: ")
        if dificuldade in {"1", "2", "3"}:
            return int(dificuldade)
        else:
            print("Valor inválido!")

def jogar_jogo():
    pontuacao = 1000
    numero_secreto = random.randint(1, 100)

    dificuldade = obter_dificuldade()
    if dificuldade == 1:
        tentativas = 20
        print(f'\nFácil: Você tem {tentativas} tentativas para descobrir o número secreto...')
    elif dificuldade == 2:
        tentativas = 10
        print(f'\nMédio: Você tem {tentativas} tentativas para descobrir o número secreto...')
    elif dificuldade == 3:
        tentativas = 5
        print(f'\nDifícil: Você tem {tentativas} tentativas para descobrir o número secreto...')

    for rodada in range(1, tentativas + 1):
        print(f'\nRODADA {rodada}')
        palpite = input("Qual é o seu palpite?\nDigite um número entre 1 e 100: ")

        if not palpite.isdigit():
            print("Digite apenas valores inteiros!")
            continue

        palpite = int(palpite)
        if palpite < 1 or palpite > 100:
            print("Fora do Intervalo!\n")
            continue

        palpite_certo = (numero_secreto == palpite)
        palpite_menor = (numero_secreto > palpite)

        if palpite_certo:
            print(f'\nParabéns! Você acertou, o número secreto é: {numero_secreto}')
            print(f'Pontuação: {pontuacao}')
            return

        if palpite_menor:
            print(f'\nSeu palpite {palpite} é MENOR que o número secreto.')
        else:
            print(f'\nSeu palpite {palpite} é MAIOR que o número secreto.')

        pontuacao -= abs(numero_secreto - palpite)

    print('\n################')
    print('# Fim de Jogo! #')
    print('################')
    print(f'O número secreto era {numero_secreto}')
    print(f'Sua pontuação: {max(pontuacao, 0)}')

jogar_jogo()