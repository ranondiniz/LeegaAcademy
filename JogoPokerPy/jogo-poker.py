import random

class Carta:
    "Representa uma carta padrão do jogo de Poker."

    def __init__(self, naipe=0, valor=2):
        self.naipe = naipe
        self.valor = valor

    naipe_nomes = ['Paus', 'Ouros', 'Copas', 'Espadas']
    valor_nomes = [None, 'Ás', '2', '3', '4', '5', '6',
                   '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']

    def __str__(self):
        return '%s de %s' % (Carta.valor_nomes[self.valor],
                             Carta.naipe_nomes[self.naipe])

    def __lt__(self, other):
        t1 = self.naipe, self.valor
        t2 = other.naipe, other.valor
        return t1 < t2

class Baralho:
    def __init__(self):
        self.cartas = []
        for naipe in range(4):
            for valor in range(1, 14):
                carta = Carta(naipe, valor)
                self.cartas.append(carta)

    def __str__(self):
        cartas = []
        for carta in self.cartas:
            cartas.append(str(carta))
        return '\n'.join(cartas)

    def pop_carta(self):
        return self.cartas.pop()

    def add_carta(self, carta):
        self.cartas.append(carta)

    def embaralhar(self):
        random.shuffle(self.cartas)

class Mao:
    "Representa as cartas que estão na mão do jogador."

    def __init__(self, label=''):
        self.cartas = []
        self.label = label

    def add_carta(self, carta):
        self.cartas.append(carta)

    def ordenar(self):
        self.cartas.sort()

class PokerGame:
    def __init__(self, player1_name, player2_name):
        self.deck = Baralho()
        self.deck.embaralhar()
        self.player1 = Mao(player1_name)
        self.player2 = Mao(player2_name)
        self.mesa = []

    def deal(self):
        for _ in range(5):
            self.player1.add_carta(self.deck.pop_carta())
            self.player2.add_carta(self.deck.pop_carta())

    def play_round(self):
        for _ in range(3):
            self.mesa.append(self.deck.pop_carta())

        print("\nCartas da mesa:")
        print("\n".join(map(str, self.mesa)))

        self.deck.pop_carta()  # Aqui se queima 1 carta
        self.mesa.append(self.deck.pop_carta())  # Abre-se a 4ª carta
        print("\nCartas da mesa (após queimar 1 carta e abrir a 4ª):")
        print("\n".join(map(str, self.mesa)))

        self.deck.pop_carta()  # Aqui se queima a 2 carta
        self.mesa.append(self.deck.pop_carta())  # Abre-se a 5ª e última carta
        print("\nCartas da mesa (após queimar 1 carta e abrir a 5ª):")
        print("\n".join(map(str, self.mesa)))

    def exchange_cards(self, player):
        print(f"\nMão atual de {player.label}:")
        for i, carta in enumerate(player.cartas):
            print(f"{i + 1}. {carta}")

        print("\nSelecione até 2 cartas para trocar (digite os índices separados por vírgula), ou deixe em branco para não trocar:")
        indices = input().strip().split(',')
        indices = [int(index) - 1 for index in indices if index.isdigit()]
        num_to_exchange = min(len(indices), 2)
        cards_to_exchange = [player.cartas[index] for index in indices]

        for carta in cards_to_exchange:
            player.cartas.remove(carta)
            player.add_carta(self.deck.pop_carta())

    def evaluate_winner(self):
        best_hands = []
        players = [self.player1, self.player2]

        for player in players:
            best_hand = player.cartas + self.mesa
            best_hand.sort(key=lambda x: x.valor, reverse=True)
            best_hands.append(best_hand[:5])

        print("\nMãos finais:")
        for i, player in enumerate(players):
            print(f"{player.label}: {', '.join(map(str, best_hands[i]))}")

        scores = [sum(card.valor for card in hand) for hand in best_hands]
        print("\nPontuações finais:")
        for i, player in enumerate(players):
            print(f"{player.label}: {scores[i]}")

        winner_index = scores.index(max(scores))
        if scores.count(scores[winner_index]) > 1:
            print("\nEmpate! O vencedor será determinado pela carta de maior valor.")
            winner_card_values = [max(hand, key=lambda x: x.valor).valor for hand in best_hands]
            winner_index = winner_card_values.index(max(winner_card_values))
        print(f"\n{players[winner_index].label} venceu esta rodada!")

# Exemplo de uso
game = PokerGame("Jogador 1", "Jogador 2")
game.deal()
game.play_round()
game.exchange_cards(game.player1)
game.exchange_cards(game.player2)
game.evaluate_winner()