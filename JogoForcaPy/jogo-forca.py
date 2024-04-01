import random

def escolher_palavra():
    palavras = [
        "python", "computador-01", "internet a fio", "programacao", "software",
        "tecnologia", "seguranca", "desenvolver", "aplicativo", "interface",
        "hardware", "framework", "servidor", "endereco", "algoritmo",
        "autenticacao", "armazenamento", "protocolo", "conectividade", "intero-perabilidade"
    ]
    return random.choice(palavras)

def mascarar_palavra(palavra, letras_acertadas):
    mascarado = ""
    for letra in palavra:
        if letra in letras_acertadas:
            mascarado += letra
        else:
            mascarado += "*"
    return mascarado

def desenhar_forca(erros):
    if erros == 0:
        print("  _______     ")
        print(" |/      |    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif erros == 1:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif erros == 2:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \\    ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif erros == 3:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \\|   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif erros == 4:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \\|/  ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif erros == 5:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \\|/  ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")
    elif erros == 6:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \\|/  ")
        print(" |       |    ")
        print(" |      /     ")
        print(" |            ")
    else:
        print("  _______     ")
        print(" |/      |    ")
        print(" |      (_)   ")
        print(" |      \\|/  ")
        print(" |       |    ")
        print(" |      / \\  ")
        print(" |            ")

def imprimir_mensagem_final(palavra_secreta, venceu):
    if venceu:
        print("\nParabéns! Você completou a palavra:", palavra_secreta)
    else:
        print("\nVocê não conseguiu! A palavra era:", palavra_secreta)

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_acertadas = set()
    tentativas_restantes = 12 if len(palavra_secreta) >= 15 else 13 - len(palavra_secreta)

    print("Bem-vindo ao Jogo da Forca!")
    print("Tente completar a palavra. Você tem {} tentativas.".format(tentativas_restantes))

    chute_completo = False
    erros = 0

    while tentativas_restantes > 0:
        print("\nPalavra secreta:", mascarar_palavra(palavra_secreta, letras_acertadas))

        if not chute_completo:
            palpite = input("Digite uma letra ou chute a palavra completa: ").lower()
            if len(palpite) > 1:
                if palpite == palavra_secreta:
                    imprimir_mensagem_final(palavra_secreta, True)
                    break
                else:
                    print("Palavra incorreta. Tente novamente.")
                    chute_completo = True
                    continue
        else:
            palpite = input("Digite uma letra: ").lower()

        if len(palpite) != 1 or not palpite.isprintable():
            print("Por favor, digite apenas um caractere válido.")
            continue

        if palpite in letras_acertadas:
           print("Você já tentou essa letra. Tente novamente.")
           continue


        if palpite in letras_acertadas:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        if palpite in palavra_secreta:
            print("Letra correta!")
            letras_acertadas.add(palpite)
        else:
            print("Letra errada. Tente novamente.")
            erros += 1

        desenhar_forca(erros)

        if set(palavra_secreta) == letras_acertadas:
            imprimir_mensagem_final(palavra_secreta, True)
            break

        tentativas_restantes -= 1

    if tentativas_restantes == 0:
        imprimir_mensagem_final(palavra_secreta, False)

    reiniciar = input("Deseja jogar novamente? (s/n): ").lower()
    if reiniciar == 's':
        jogar_forca()

jogar_forca()
