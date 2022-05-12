# a game of coin flipping - heads or tails where the probability of heads is 0.5 and the probability of tails is 0.5 
# there are two players, each have 100 money, and each player can bet 1 money, if heads is chosen, player 1 wins, if tails is chosen, player 2 wins
# when either player has no money, the game ends
# the game ends when either player has no money
import random

class Player:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def score(self,player2):
        self.money =  self.money + 1
        player2.money = player2.money - 1

class Game:
    turns = 0
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self):
        while self.player1.money > 0 and self.player2.money > 0:
            self.turns = self.turns + 1
            if self.flip() == "heads":
                self.player1.score(self.player2)
            else:
                self.player2.score(self.player1)
            # if(self.player1.money == 0):
            #     print("Player 1 has no money left")
            #     print("Turns:", self.turns)
            # if(self.player2.money == 0):
            #     print("Player 2 has no money left")
            #     print("Turns:", self.turns)
            if(self.player1.money == 0 or self.player2.money == 0):
                if(self.player1.money == 0):
                    self.add_result_to_csv([self.player2.name, self.turns])
                else:
                    self.add_result_to_csv([self.player1.name, self.turns])
    
    def flip(self):
        flip = random.randint(1,2)
        if flip == 1:
            return "heads"
        else:
            return "tails"
    
    def add_result_to_csv(self, result):
        # open a file for writing, if it doesn't exist, create it, result is a list add the result to the file
        with open("results.csv", "a") as f:
            f.write(result[0] + "," + str(result[1]) + "\n")

for i in range(0,10000): 
    game = Game(Player("player1", 100), Player("player2", 100))
    game.start()

