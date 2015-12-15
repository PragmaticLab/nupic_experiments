import sys
import importlib
import csv
import random
from Queue import Queue

from nupic.frameworks.opf.modelfactory import ModelFactory

from model_params import rps_model_params
from generate_data import RockPaperScissors

SIM_COUNT = 10000

predictionSteps = 1
model = ModelFactory.create(rps_model_params.MODEL_PARAMS)
model.enableInference({'predictedField': 'winner'})

game = RockPaperScissors()

resultFile = open("output.txt", 'w', 0)
resultWriter = csv.writer(resultFile)
resultWriter.writerow(["prediction","actual"])
resultWriter.writerow(["int","int"])
resultWriter.writerow(["",""])

count = 0
lastWinner = "draw"
while count < SIM_COUNT:
	player1 = int(random.random() * 3)
	player2 = int(random.random() * 3)
	winner = game.processRound(player1, player2)
	row = {
		"player1": game.roles[player1],
		"player2": game.roles[player2],
		"winner": lastWinner
	}
	result = model.run(row)
	futurePrediction = result.inferences["multiStepBestPredictions"][predictionSteps]
	correct = futurePrediction == winner

	# print "{0} {1}: winner: {2}".format(game.roles[player1], game.roles[player2], futurePrediction)
	resultWriter.writerow([futurePrediction, winner, correct])
	
	lastWinner = winner
	if count % 100 == 0:
		print "count: " + str(count)
	count += 1
