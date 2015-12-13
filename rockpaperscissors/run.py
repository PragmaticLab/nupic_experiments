import sys
sys.path.append('model_0')
import model_params
from nupic.frameworks.opf.modelfactory import ModelFactory
from Queue import Queue
import csv
from generate_data import RockPaperScissors
import random

SIM_COUNT = 3000

predictionSteps = 1
model = ModelFactory.create(model_params.MODEL_PARAMS)
model.enableInference({'predictedField': 'scoreBeforeDuel'})

game = RockPaperScissors()

resultFile = open("output.txt", 'w', 0)
resultWriter = csv.writer(resultFile)
resultWriter.writerow(["prediction","actual"])
resultWriter.writerow(["int","int"])
resultWriter.writerow(["",""])

predictionQueue = Queue(maxsize=predictionSteps + 2)
for i in range(predictionSteps):
	predictionQueue.put(-1)

count = 0
while count < SIM_COUNT:
	player1 = int(random.random() * 3)
	player2 = int(random.random() * 3)
	scoreBeforeDuel = game.score
	result = model.run({
		"player1": player1,
		"player2": player2,
		"scoreBeforeDuel": scoreBeforeDuel
	})
	futurePrediction = result.inferences["multiStepBestPredictions"][predictionSteps]
	predictionQueue.put(futurePrediction)
	prediction = predictionQueue.get()
	resultWriter.writerow([prediction, game.score])
	game.processRound(player1, player2)
	if count % 100 == 0:
		print "count: " + str(count)
	count += 1
