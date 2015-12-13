import csv
import math
import random

ROWS = 10000

class RockPaperScissors:
    def __init__(self):
        self.score = 0
        self.roles = {
            0: "rock",
            1: "paper",
            2: "scissors"
        }

    def rockPaperScissors(self, role1, role2):
        if role1 == role2:
            return 0
        if role1 == "rock" and role2 == "paper":
            return -1
        if role1 == "rock" and role2 == "scissors":
            return 1
        if role1 == "paper" and role2 == "scissors":
            return -1
        if role1 == "paper" and role2 == "rock":
            return 1
        if role1 == "scissors" and role2 == "rock":
            return -1
        if role1 == "scissors" and role2 == "paper":
            return 1


    def processRound(self, player1, player2):
        self.score += self.rockPaperScissors(self.roles[player1], self.roles[player2])
        if self.score >= 5:
            self.score = 5
        elif self.score <= -5:
            self.score = -5


def run(filename="rps.csv"):
    print "Generating tan data into %s" % filename
    fileHandle = open(filename,"w")
    writer = csv.writer(fileHandle)
    writer.writerow(["player1", "player2", "scoreBeforeDuel"])
    writer.writerow(["int", "int", "int"])
    writer.writerow(["", "", ""])

    count = 0
    game = RockPaperScissors()
    while count < ROWS:
        player1 = int(random.random() * 3)
        player2 = int(random.random() * 3)
        score_before_duel = game.score
        game.processRound(player1, player2)
        writer.writerow([player1, player2, score_before_duel])
        count += 1

    fileHandle.close()
    print "Generated %i rows of output data into %s" % (ROWS, filename)

if __name__ == "__main__":
  run()
