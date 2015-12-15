import csv
import math
import random

ROWS = 200

class RockPaperScissors:
    def __init__(self):
        self.score = 0
        self.roles = {
            0: "rock",
            1: "paper",
            2: "scissors"
        }

    def rockPaperScissors(self, role1, role2):
        winner = "draw"
        if role1 == "rock" and role2 == "paper":
            winner = "player2"
        elif role1 == "rock" and role2 == "scissors":
            winner = "player1"
        elif role1 == "paper" and role2 == "scissors":
            winner = "player2"
        elif role1 == "paper" and role2 == "rock":
            winner = "player1"
        elif role1 == "scissors" and role2 == "rock":
            winner = "player2"
        elif role1 == "scissors" and role2 == "paper":
            winner = "player1"
        return winner


    def processRound(self, player1, player2):
        return self.rockPaperScissors(
            self.roles[player1], 
            self.roles[player2]
        )


def run(filename="rps.csv"):
    print "Generating rps data into %s" % filename
    fileHandle = open(filename,"w")
    writer = csv.writer(fileHandle)
    writer.writerow(["player1", "player2", "winner"])
    writer.writerow(["string", "string", "string"])
    writer.writerow(["", "", ""])

    count = 0
    game = RockPaperScissors()
    lastWinner = ""
    while count < ROWS:
        player1 = int(random.random() * 3)
        player2 = int(random.random() * 3)
        # score_before_duel = game.score
        winner = game.processRound(player1, player2)
        writer.writerow([game.roles[player1], game.roles[player2], lastWinner])
        count += 1
        lastWinner = winner

    fileHandle.close()
    print "Generated %i rows of output data into %s" % (ROWS, filename)

if __name__ == "__main__":
  run()
