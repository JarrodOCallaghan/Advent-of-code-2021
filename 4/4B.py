import dataset
import datasetTest

cards, draw = dataset.main()
# cards, draw = datasetTest.main()

# print(len(cards))
# print(draw)


class Card:
    def __init__(self, numbers, id):
        self.numbers = numbers
        self.marks = numbers.copy()
        self.bingo = False
        self.entry = id
        self.last_number = None

    def mark_number(self, draw):
        if self.marks == []:
            self.marks = self.numbers.copy()
        for i in range(len(self.marks)):
            for j in range(len(self.marks[0])):
                # print(f'{i}, {j}, {self.marks[i][j]} = {draw}?')
                if self.marks[i][j] == draw:
                    # print(self.marks[i][j])
                    print(f"Card {self.entry} marked {draw}")
                    self.marks[i][j] = "X"
                    self.last_number = draw

                    # print(self.marks[i][j])
                    self.__check_bingo()

    def __check_bingo(self):
        # We are assuming each card is the same depth
        # Depth is -1 to account for array index
        width = len(self.marks)
        depth = len(self.marks[0])
        if not self.bingo:
            for i in range(width):
                counter = 0
                # print(self.marks[i][0])
                #if self.marks[i][0] == "X":
                for j in range(depth):
                    if self.marks[i][j] == "X":
                        counter += 1
                if counter == 5:
                    self.bingo = True
            for i in range(depth):
                counter = 0
                #if self.marks[0][i] == "X":
                for j in range(width):
                    if self.marks[j][i] == "X":
                        counter += 1
                if counter == 5:
                    print("BINGO!")
                    self.bingo = True
                    print(f"Score is: {self.get_score()}")

    def get_score(self):
        return self.get_unmarked_sum() * self.last_number

    def get_bingo(self):
        return self.bingo

    def get_unmarked_sum(self):
        width = len(self.marks)
        depth = len(self.marks[0])
        score = 0
        for i in range(width):
            for j in range(depth):
                if self.marks[i][j] != "X":
                    score += self.marks[i][j]
        return score

    def dispaly_card(self):
        # print('\n')
        for i in range(len(self.marks)):
            print(f"{i}: {self.marks[i]}")

    def get_id(self):
        return self.entry

    def get_winning_stats(self):
        print("Winner")
        unmarked_sum = self.get_unmarked_sum()
        print(f"ID: {self.entry}, {unmarked_sum} * {self.last_number}")
        print(unmarked_sum * self.last_number)


class Games:
    def __init__(self):
        self.games = []
        self.winner = None
        self.entries = 0
        self.completed_cards = []

    def create_game(self, card):
        card = Card(card, self.entries)
        self.entries += 1
        self.games.append(card)

    def draw_number(self, draw):
        for card in self.games:
            if card.get_bingo() is True:
                pass
            else:
                card.mark_number(draw)
                if card.get_bingo() is True:
                    if len(self.completed_cards) < 99:
                        print(f'Removing card')
                        self.completed_cards.append(card)
                    else:
                        self.winner = card
                        return card

    def count_cards(self):
        return len(self.games)

    def display_games(self):
        for game in self.games:
            game.dispaly_card()

    def get_winner(self):
        return self.winner


print("Creating games")
game = Games()
print("Creating cards")
for card in cards:
    game.create_game(card)
print(f"Created: {game.count_cards()} cards")
# print(game.display_games())
print("Starting draw")

for number in draw:
    if game.get_winner() is None:
        print(f"Drawed: {number}")
        game.draw_number(number)
    else:
        break
print(game.get_winner().dispaly_card())
print(game.get_winner().get_winning_stats())
